from sqlalchemy import create_engine,text

username = "postgres"
password = "atratr"
host = "localhost"
port = "5432"
db = "columbia_housing"

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db}"
)

create_sql = """
CREATE TABLE IF NOT EXISTS rent_income (
    year INT,
    median_rent INT,
    median_income INT
)
"""

with engine.begin() as conn:
    conn.execute(text(create_sql))

print("table created")