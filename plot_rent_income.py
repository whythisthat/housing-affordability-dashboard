import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

username = "postgres"
password = "atratr"
host = "localhost"
port = "5432"
db = "columbia_housing"

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db}"
)

query = "SELECT * FROM rent_income ORDER BY year"
df = pd.read_sql(query, engine)

plt.plot(df["year"], df["median_rent"], label="Rent")
plt.plot(df["year"], df["median_income"], label="Income")

plt.title("Columbia Rent vs Income")
plt.xlabel("Year")
plt.ylabel("Value")
plt.legend()

plt.show()
