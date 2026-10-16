import os
import pandas as pd
from src.database import engine, init_db

def run_etl(excel_filepath=str):
    print("Initializing PostgreSQL database in 'hoi4resources' ...")
    init_db()

    print(f"Parsing HOI4 Excel Sheet from {excel_filepath}")
    df = pd.read_excel(excel_filepath, sheet_name='HOI4v 1.14.4 countries')

    df.columns = [col.strip() for col in df.columns]

    print("Extracting and lodaing unique countries into 'dim_country' ...")
    df_countries = df[["Owner Tag", "Country Name"]].drop_duplicates().dropna()
    df_countries.columns = ["country_tag", "country_name"]
    df_countries["country_tag"] = df_countries["country_tag"].astype(str).str.strip()
    df_countries["country_name"] = df_countries["country_name"].astype(str).str.strip()

    df_countries.to_sql("dim_country", engine, if_exists="append", index=False)

    print("Mapping state metrics and loading into 'fact_state_1_14_5' ...")
    column_mapping = {
        "ID": "state_id",
        "State Name": "state_name",
        "Owner Tag": "owner_tag",
        "State Status": "state_status",
        "State category": "state_category",
        "vp": "victory_points",
        "Provinces": "provinces_count",
        "population": "population",
        "infra": "infrastructure",
        "* Unadjusted Building slots": "building_slots",
        "MIC": "military_factories",
        "NIC": "naval_factories",
        "CIC": "civilian_factories",
        "Total Factories": "total_factories",
        "Base Oil": "base_oil",
        "Base Alum": "base_aluminum",
        "Base Rub": "base_rubber",
        "Base Tung": "base_tungsten",
        "Base Steel": "base_steel",
        "Base Chrom": "base_chromium",
        "Total Base Resources": "total_base_resources",
    }

    df_facts = df[list(column_mapping.keys())].rename(columns=column_mapping)
    df_facts["state_id"] = df_facts["state_id"].astype(int)
    df_facts["owner_target"] = df_facts["owner_tag"].astype(str).str.strip()
    df_facts.to_sql("fact_state_1_14_5", engine, if_exists="append", index=False)
    print("✅ Ingestion complete! All state resource records loaded into PostgreSQL.")

if __name__ == "__main__":
    EXCEL_PATH = os.path.join("data", "HOI4 1.14.5 resource history spreadsheet -.xlsx")
    run_etl(EXCEL_PATH)