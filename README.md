# HOI4 Resource Catalogue & Database Analysis

An end-to-end data engineering and analytics platform built for **Hearts of Iron IV (v1.14.5)** state and country-level strategic data. This repository extracts, transforms, and loads game metrics into a structured PostgreSQL database, delivering interactive visualizations and analytical insights via Python, Pandas, and Plotly.

---

## 💡 Key HOI4 Terms & Domain Knowledge

To better understand the dataset, schema, and analysis, here are the essential Hearts of Iron IV concepts used across this repository:

* **State (`fact_state_1_14_5`)**: The core administrative unit on the HOI4 map. Each state has an owner nation, population, building slots, and raw resource deposits.
* **Province (`provinces_count`)**: The smaller sub-units that make up a single state. Military units move across individual provinces, but economy and resource extraction are managed at the state level.
* **Population Density (`population_density`)**: Calculated as total state population divided by province count ($\text{Population} / \text{Provinces}$). This metric highlights heavily urbanized regions versus sparse wilderness.
* **Country Tag (`country_tag` / `owner_tag`)**: A unique 3-letter identifier used internally by HOI4 to represent sovereign nations (e.g., `GER` for Germany, `SOV` for Soviet Union, `USA` for United States).
* **Strategic Resources (`base_steel`, `base_oil`, etc.)**: Raw material inputs required to build and maintain military equipment. High-yield resource states represent strategic control points.

---

## 📌 Core Features

- **Relational Data Schema**: Fully normalized PostgreSQL structure featuring a central fact table (`fact_state_1_14_5`) linked to country dimension metadata (`dim_country`).
- **Generated Database Columns**: Automated population density metrics calculated at the database engine level via PostgreSQL generated columns.
- **Interactive Analytics**: Rich Plotly scatter, bubble, and bar charts analyzing strategic resource distribution, population density, and regional concentration.
