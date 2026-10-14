import os
import pandas as pd
from src.database import engine, init_db

def run_etl(excel_filepath=str):
    print("Initializing PostgreSQL database in 'hoi4resources' ...")
    init_db()

    print(f"Parsing HOI4 Excel Sheet from {excel_filepath}")
    df = pd.read_excel(excel_filepath, sheet_name='HOI4v 1.14.4 countries')

    df.columns = [col.strip() for col in df.columns()]

    print("Extracting and lodaing unique countries into 'dim_country' ...")
    df_countries = df[["Owner Tag", "Country Name"]].drop_duplicates().dropna()
    df_countries.columns = ["country_tag", "country_name"]
    df_countries["country_tag"] = df_countries["country_tag"].astype(str).str.strip()
    df_countries["country_name"] = df_countries["country_name"].astype(str).str.strip()

    df_countries.tosql("dim_country", engine, if_exists="append", index=False)

    