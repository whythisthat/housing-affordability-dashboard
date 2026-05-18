import pandas as pd

df = pd.read_csv("scripts/data/county_court_issued_2000_2018.csv")

richland = df[
    (df["state"] == "South Carolina") &
    (df["county"] == "Richland County")
]

clean = richland[["year", "filings_observed"]]

clean.to_csv("scripts/data/county_court_issued_2000_2018.csv", index=False)

print(clean.head())