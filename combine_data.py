import pandas as pd

income_df = pd.read_csv("data/ACSDT1Y2024.B19013-2026-05-11T192606.csv")
rent_df = pd.read_csv("data/ACSDT1Y2024.B19013-2026-05-11T192606.csv")

income_df = income_df[[
    "Label (Grouping)",
    "Richland County, South Carolina!!Estimate"
]]

rent_df = rent_df[[
    "Label (Grouping)",
    "Richland County, South Carolina!!Estimate"
]]

income_df.columns = ["label", "income"]
rent_df.columns = ["label", "rent"]

income_df["income"] = income_df["income"].replace(",", "", regex=True)
rent_df["rent"] = rent_df["rent"].replace(",", "", regex=True)

income_df["income"] = pd.to_numeric(income_df["income"])
rent_df["rent"] = pd.to_numeric(rent_df["rent"])

combined_df = pd.concat([income_df, rent_df], axis=1)

print(combined_df)