import pandas as pd
from src.database import engine

def get_top_resources(limit: int = 10) -> pd.DataFrame:
    query = f"""
    SELECT 
        c.country_name,
        SUM(s.base_oil) AS total_oil,
        SUM(s.base_aluminum) AS total_aluminum,
        SUM(s.base_rubber) AS total_rubber,
        SUM(s.base_tungsten) AS total_tungsten,
        SUM(s.base_steel) AS total_steel,
        SUM(s.base_chromium) AS total_chromium,
        SUM(s.total_base_resources) AS total_resources
    FROM fact_state_1_14_5 s
    JOIN dim_country c ON s.owner_tag = c.country_tag
    GROUP BY c.country_name
    ORDER BY total_resources DESC
    LIMIT {limit};
    """
    return pd.read_sql(query, engine)

if __name__ == "__main__":
    print("Top 5 Resources Powers:")
    print(get_top_resource_countries(5)[["country_name", "total_resources", "total_steel", "total_oil"]])