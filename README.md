# Argentina Oil & Gas Production Analysis



## Project Overview



This project analyzes oil and gas well production data from Argentina using a multi-year dataset covering 2021-2026.



The project focuses on preparing large production datasets for analysis by identifying schema inconsistencies between annual source files, standardizing the data structure with Python and Pandas, and developing an interactive Power BI dashboard for production analysis.



The project demonstrates practical data-analysis and data-engineering skills applied to a real-world, high-volume dataset.



---



## Project Objectives



The primary objectives of this project are to:



- Analyze multi-year oil and gas production data.

- Identify inconsistencies between yearly source files.

- Standardize yearly datasets into a common schema.

- Validate column structure before combining data.

- Create unique identifiers where required.

- Prepare cleaned data for downstream analytical workflows.

- Build an interactive Power BI dashboard for production analysis.

- Document data-quality and transformation decisions.



---



## Data Scope



The source data covers:



**2021-2026**



The annual CSV files contain detailed well-production information including:



- Oil production

- Gas production

- Water production

- Water injection

- Gas injection

- CO2 injection

- Well information

- Extraction type

- Well status

- Formation

- Depth

- Operator/company

- Basin

- Province

- Resource type

- Production date



The standardized analytical schema contains **39 columns**.



---



## Data Engineering Challenge



One of the major challenges identified during the project was that the annual source files did not have completely consistent schemas.



Python was used to compare the column structure of the six yearly datasets and identify differences in:



- Column counts

- Missing columns

- Column names

- Column positions

- Column order



A key inconsistency involved the `id` field.



Some yearly datasets did not contain the `id` column required by the standardized schema.



To address this problem, the transformation process generates a unique numeric identifier for records where the source file does not provide one.



Example:



```text

20210000001



Data Preparation Workflow



This approach allows the standardized datasets to maintain a usable row identifier while preserving the original production information.

Raw Annual CSV Files

&#x20;       

&#x09;|

&#x20;       v

Python Schema Inspection

&#x20;       |

&#x20;       v

Column Validation

&#x20;       |

&#x20;       v

Schema Standardization

&#x20;       |

&#x20;       v

Unique ID Generation

&#x20;       |

&#x20;       v

Standardized 39-Column Files

&#x20;       |

&#x20;       v

Analytical Dataset

&#x20;       |

&#x20;       v

Power BI



Python Scripts

fixing_raw_csvs.py

Compares the headers of the annual datasets from 2021 through 2026.

The script checks columns by position and identifies differences between yearly schemas.

fixing_raw_csvs_header.py

Standardizes the annual datasets to a common 39-column schema.

The script:

- Detects missing columns.

- Adds missing fields when necessary.

- Generates an ID when the source dataset does not contain one.

- Enforces a consistent column order.

- Writes standardized CSV files to the fixed directory.

fixing_raw_csvs_id.py

Refines the ID-generation process by creating numeric unique identifiers compatible with an integer-based destination field.

For example:

&#x20;Year: 2021

Row: 1

Generated ID: 20210000001



This represents an important data-engineering step because the transformation was adjusted to meet the required destination data type.

Power BI Dashboard

The project includes the Power BI report:

2021-2026--ARGENTINA-OIL&GAS-PRODUCTION.pbix

The dashboard provides an analytical interface for exploring the prepared oil and gas production data.

Technologies Used

- Python

- Pandas

- CSV

- Power BI

- Git

- GitHub

The data-preparation scripts were also designed with downstream warehouse loading in mind.

Large Dataset Management

The original and standardized CSV datasets are intentionally excluded from this GitHub repository.

Several source files exceed hundreds of megabytes, making them unsuitable for normal GitHub version control.

Instead, this repository contains the transformation logic and analytical deliverables necessary to demonstrate how the data was inspected, standardized, and analyzed.

This approach keeps the repository lightweight while preserving the reproducible logic used in the project.

Data Quality Approach

The project treats data preparation as part of the analytical process rather than assuming that yearly files can automatically be combined.

Before integration, the datasets are evaluated for structural consistency.

This includes validating:

- Schema differences

- Missing columns

- Column ordering

- Record identifiers

- Data compatibility across years

This reduces the risk of combining incompatible datasets and producing misleading analytical results.

Repository Contents



argentina-oil-gas-production-analysis/

|

|-- README.md

|-- .gitignore

|

|-- fixing_raw_csvs.py

|-- fixing_raw_csvs_header.py

|-- fixing_raw_csvs_id.py

|

|-- 2021-2026--ARGENTINA-OIL&GAS-PRODUCTION.pbix

Large CSV datasets and the local fixed directory are excluded through .gitignore.

Project Skills Demonstrated

This project demonstrates practical experience with:

- Large dataset management

- Python data processing

- Pandas

- Schema validation

- Data-quality investigation

- Multi-year dataset integration

- Data transformation

- Unique identifier generation

- Power BI

- Analytical problem solving

- Technical documentation

- Git and GitHub version control

Author

Miguel Angel Zapata

Data Analytics Portfolio Project








