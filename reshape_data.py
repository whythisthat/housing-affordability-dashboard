import pandas as pd

income_df = pd.read_csv("data/ACSDT1Y2024.B19013-2026-05-11T192606.csv")
rent_df = pd.read_csv("data/ACSDT1Y2024.B19013-2026-05-11T192606.csv")

income = income_df.iloc[0, 1]
rent = rent_df.iloc[0, 1]

income = float(str(income).replace(",", ""))
rent = float(str(rent).replace(",", ""))

df = pd.DataFrame({
    "income": [income],
    "rent": [rent]
})

df["rent_to_income_ratio"] = df["rent"] / df["income"]

print(df)