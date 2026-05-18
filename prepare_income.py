import pandas as pd

df = pd.read_csv("data/ACSDT1Y2024.B19013-2026-05-11T192606.csv")

df = df[[
    "Label (Grouping)",
    "Richland County, South Carolina!!Estimate"
]]

df.columns = ["label", "income"]

df["income"] = df["income"].replace(",", "", regex=True)
df["income"] = pd.to_numeric(df["income"])

print(df)
print(df.dtypes)