import pandas as pd

rent_data = {
    "year": [2010, 2015, 2020, 2023],
    "rent": [790, 890, 1030, 1250]
}

df = pd.DataFrame(rent_data)

print(df)