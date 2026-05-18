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

income_df = pd.read_csv("data/income_fred.csv")

income_df.columns = ["year", "income"]

income_df["year"] = pd.to_datetime(income_df["year"]).dt.year
income_df["income"] = pd.to_numeric(income_df["income"], errors="coerce")

income_df = income_df.dropna()
income_df = income_df[income_df["year"] >= 2010]

rent_df = pd.DataFrame({
    "year": [2010, 2015, 2020, 2023],
    "rent": [790, 890, 1030, 1250]
})

merged_df = pd.merge(income_df, rent_df, on="year", how="inner")

merged_df["annual_rent"] = merged_df["rent"] * 12

merged_df["rent_burden_ratio"] = (
    merged_df["annual_rent"] / merged_df["income"]
)

merged_df.to_sql(
    "housing_trends",
    engine,
    if_exists="replace",
    index=False
)

print(merged_df)
print("table saved")