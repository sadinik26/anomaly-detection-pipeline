import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///anomalies.db"

engine = create_engine(DATABASE_URL)

query = """

SELECT *

FROM weather_features

"""

df = pd.read_sql(query, engine)

print(df)