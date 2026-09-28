"""
Fix the yearly oil & gas production CSVs so all 6 years have an identical
39-column schema before loading into Snowflake.

Root cause confirmed: the 2021 (and likely 2022, 2023, 2025, 2026) files
have 38 columns — they're missing the "id" column that 2024's file has.
This script adds a synthetic, unique "id" to any file that's missing it,
so every year has a genuinely usable row identifier instead of a NULL.

Real filenames are simply 2021.csv, 2022.csv, etc. (not the long
Spanish names) — update FILE_PATHS below to match your actual folder.
"""

import pandas as pd
from pathlib import Path

# ---------------------------------------------------------------------------
# CONFIG — edit this folder path if needed
# ---------------------------------------------------------------------------

SOURCE_DIR = r"C:\Users\mexar\OneDrive\DE_Academy\CSVs\Producción de petróleo y gas por pozo (Capítulo IV)"

YEARS = [2021, 2022, 2023, 2024, 2025, 2026]

# The full canonical 39-column schema (from the working 2024 file, plus "id")
CANONICAL_COLUMNS = [
    "idempresa", "anio", "mes", "idpozo", "prod_pet", "prod_gas", "prod_agua",
    "iny_agua", "iny_gas", "iny_co2", "iny_otro", "tef", "vida_util",
    "tipoextraccion", "tipoestado", "tipopozo", "observaciones", "fechaingreso",
    "rectificado", "habilitado", "idusuario", "empresa", "sigla", "formprod",
    "profundidad", "formacion", "idareapermisoconcesion", "areapermisoconcesion",
    "idareayacimiento", "areayacimiento", "cuenca", "provincia",
    "tipo_de_recurso", "proyecto", "clasificacion", "subclasificacion",
    "sub_tipo_recurso", "fecha_data", "id",
]

OUTPUT_DIR = str(Path(SOURCE_DIR) / "fixed")

# ---------------------------------------------------------------------------
# SCRIPT
# ---------------------------------------------------------------------------

def main():
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    for year in YEARS:
        path = Path(SOURCE_DIR) / f"{year}.csv"
        if not path.exists():
            print(f"--- {year} --- SKIPPED: file not found at {path}")
            continue

        df = pd.read_csv(path, encoding="utf-8-sig")  # utf-8-sig strips BOM
        found_cols = list(df.columns)
        missing = [c for c in CANONICAL_COLUMNS if c not in found_cols]

        print(f"--- {year} --- {len(found_cols)} columns found, missing: {missing or 'none'}")

        if "id" in missing:
            # Generate a synthetic unique NUMERIC id (year + zero-padded row
            # number combined into one integer), since Snowflake's id column
            # is type INT and can't accept a string like "2021-1".
            # e.g. year 2021, row 1 -> 20210000001
            df["id"] = [int(f"{year}{i+1:07d}") for i in range(len(df))]
            print(f"  Generated synthetic numeric 'id' column ({len(df):,} unique values)")

        # Fill any other missing columns with NULL, then enforce column order
        for col in CANONICAL_COLUMNS:
            if col not in df.columns:
                df[col] = None
        df = df[CANONICAL_COLUMNS]

        out_path = Path(OUTPUT_DIR) / f"{year}.csv"
        df.to_csv(out_path, index=False, encoding="utf-8")
        print(f"  Saved: {out_path} ({len(df):,} rows, {len(df.columns)} columns)")
        print()

    print("Done. Upload the files from the 'fixed' folder to S3, replacing the originals.")


if __name__ == "__main__":
    main()