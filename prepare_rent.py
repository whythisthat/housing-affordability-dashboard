import pandas as pd

df = pd.read_csv("data/ACSDT1Y2024.B19013-2026-05-11T192606.csv")

df = df[[
    "Label (Grouping)",
    "Richland County, South Carolina!!Estimate"
]]

df.columns = ["label", "rent"]

df["rent"] = df["rent"].replace(",", "", regex=True)
df["rent"] = pd.to_numeric(df["rent"])

print(df)
print(df.dtypes)