import pandas as pd

df = pd.read_csv("data/income_fred.csv")

df.columns = ["year", "income"]

df["year"] = pd.to_datetime(df["year"]).dt.year

df["income"] = pd.to_numeric(df["income"], errors="coerce")

df = df.dropna()

df = df[df["year"] >= 2005]

print(df.head())
print(df.tail())
print(df.dtypes)