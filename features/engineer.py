import pandas as pd
from sqlalchemy import create_engine

# ------------------------------------
# Database Connection
# ------------------------------------

DATABASE_URL = "sqlite:///anomalies.db"

engine = create_engine(DATABASE_URL)

# ------------------------------------
# Load Data
# ------------------------------------

query = """
SELECT *
FROM weather_data
ORDER BY timestamp
"""

df = pd.read_sql(query, engine)

print("\nRaw Dataset\n")
print(df)

# ------------------------------------
# Feature Engineering
# ------------------------------------

# Rolling Mean (3 observations)
df["rolling_mean"] = df["temperature"].rolling(window=3).mean()

# Rolling Standard Deviation
df["rolling_std"] = df["temperature"].rolling(window=3).std()

# Previous Temperature
df["lag_1"] = df["temperature"].shift(1)

# Hour Feature
df["timestamp"] = pd.to_datetime(df["timestamp"])

df["hour"] = df["timestamp"].dt.hour

# Day of Week
df["day_of_week"] = df["timestamp"].dt.dayofweek

print("\nFeature Engineered Dataset\n")
print(df)