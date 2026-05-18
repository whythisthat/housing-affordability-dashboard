import pandas as pd

def clean(file, year):
    df = pd.read_csv(file)

    df["Estimate"] = (
        df["Richland County, South Carolina!!Estimate"]
        .str.replace(",", "")
    )
    df["Estimate"] = pd.to_numeric(df["Estimate"])

    df["year"] = year

    return df[["year", "Label (Grouping)", "Estimate"]]


df2010 = clean("scripts/data/ACSDT5Y2010.B25070-2026-05-17T032358.csv", 2010)
df2015 = clean("scripts/data/ACSDT5Y2015.B25070-2026-05-17T032342.csv", 2015)
df2020 = clean("scripts/data/ACSDT5Y2020.B25070-2026-05-17T032324.csv", 2020)

df = pd.concat([df2010, df2015, df2020])


burden = df[
    df["Label (Grouping)"].str.contains(
        "30.0 to 34.9|35.0 to 39.9|40.0 to 49.9|50.0 percent",
        na=False
    )
]

total = df[df["Label (Grouping)"] == "Total:"].groupby("year")["Estimate"].sum()

burden_sum = burden.groupby("year")["Estimate"].sum()

rate = (burden_sum / total).reset_index()
rate.columns = ["year", "rent_burden_30plus"]

rate.to_csv("scripts/data/rent_burden_page2.csv", index=False)

print(rate)