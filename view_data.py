from sqlalchemy import create_engine, text

username = "postgres"
password = "atratr"
host = "localhost"
port = "5432"
db = "columbia_housing"

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db}"
)

query = "SELECT * FROM rent_income ORDER BY year"

with engine.connect() as conn:
    result = conn.execute(text(query))

    for row in result:
        print(row)
