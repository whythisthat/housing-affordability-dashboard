from sqlalchemy import create_engine, text

username = "postgres"
password = "atratr"
host = "localhost"
port = "5432"
db = "columbia_housing"

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db}"
)

insert_sql = """
INSERT INTO rent_income (year, median_rent, median_income)
VALUES
(2015, 850, 42000),
(2018, 980, 45000),
(2020, 1100, 47000),
(2023, 1250, 51000)
"""

with engine.begin() as conn:
    conn.execute(text(insert_sql))

print("data inserted")