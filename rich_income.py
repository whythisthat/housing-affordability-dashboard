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


df2010 = clean("scripts/data/ACSDT5Y2010.B19013-2026-05-17T040522.csv", 2010)
df2015 = clean("scripts/data/ACSDT5Y2015.B19013-2026-05-17T040507.csv", 2015)
df2020 = clean("scripts/data/ACSDT5Y2020.B19013-2026-05-17T040450.csv", 2020)

df = pd.concat([df2010, df2015, df2020])

income = df[
    df["Label (Grouping)"].str.contains(
        "Median household income",
        na=False
    )
]

clean = income[["year", "Estimate"]]
clean.columns = ["year", "income"]

clean.to_csv("scripts/data/income_page2.csv", index=False)

print(clean)