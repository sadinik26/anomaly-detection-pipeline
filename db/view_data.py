from sqlalchemy import create_engine
import pandas as pd

DATABASE_URL = "sqlite:///anomalies.db"

engine = create_engine(DATABASE_URL)

query = """
SELECT *
FROM weather_data
ORDER BY id DESC
"""

df = pd.read_sql(query, engine)

print(df)