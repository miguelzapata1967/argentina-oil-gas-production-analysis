"""
Compare the headers of all 6 yearly oil & gas CSVs side-by-side,
aligned by column position, so any mismatch (missing, renamed, or
reordered column) is immediately visible.

Prints a table: one row per column position, one column per year.
Where a year's column name differs from the others at that position,
it's flagged with a marker.
"""

from pathlib import Path

SOURCE_DIR = r"C:\Users\mexar\OneDrive\DE_Academy\CSVs\Producción de petróleo y gas por pozo (Capítulo IV)\fixed"
YEARS = [2021, 2022, 2023, 2024, 2025, 2026]


def get_header(path: Path) -> list[str]:
    with open(path, "r", encoding="utf-8-sig") as f:
        return f.readline().strip().split(",")


def main():
    headers = {}
    for year in YEARS:
        path = Path(SOURCE_DIR) / f"{year}.csv"
        if not path.exists():
            print(f"{year}: FILE NOT FOUND at {path}")
            continue
        headers[year] = get_header(path)

    if not headers:
        print("No files found — check SOURCE_DIR.")
        return

    max_len = max(len(h) for h in headers.values())
    years_found = list(headers.keys())

    # Column widths for pretty printing
    col_width = 26

    # Header row
    print(f"{'#':<4}" + "".join(f"{y:<{col_width}}" for y in years_found))
    print("-" * (4 + col_width * len(years_found)))

    mismatches = []
    for i in range(max_len):
        row_vals = []
        vals_at_pos = []
        for y in years_found:
            val = headers[y][i] if i < len(headers[y]) else "(missing)"
            vals_at_pos.append(val)
            row_vals.append(f"{val:<{col_width}}")
        # Flag if not all values at this position match
        flag = " <-- DIFFERS" if len(set(vals_at_pos)) > 1 else ""
        if flag:
            mismatches.append(i + 1)
        print(f"{i+1:<4}" + "".join(row_vals) + flag)

    print()
    print(f"Total column positions compared: {max_len}")
    print(f"Column counts per year: " + ", ".join(f"{y}={len(headers[y])}" for y in years_found))
    print(f"Positions with mismatches: {mismatches if mismatches else 'none'}")


if __name__ == "__main__":
    main()