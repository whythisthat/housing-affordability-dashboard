import pandas as pd
from sqlalchemy import create_engine

username = "postgres"
password = "atratr"
host = "localhost"
port = "5432"
db = "columbia_housing"

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db}"
)

df = pd.read_csv("scripts/data/county_court_issued_2000_2018.csv")

df.to_sql(
    "evictions_trends",
    engine,
    if_exists="replace",
    index=False
)

print(df.head())
print("loaded")