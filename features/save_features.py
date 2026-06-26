import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///anomalies.db"

engine = create_engine(DATABASE_URL)

query = """
SELECT *
FROM weather_data
ORDER BY timestamp
"""

df = pd.read_sql(query, engine)

# --------------------------
# Feature Engineering
# --------------------------

df["rolling_mean"] = df["temperature"].rolling(3).mean()

df["rolling_std"] = df["temperature"].rolling(3).std()

df["lag_1"] = df["temperature"].shift(1)

df["timestamp"] = pd.to_datetime(df["timestamp"])

df["hour"] = df["timestamp"].dt.hour

df["day_of_week"] = df["timestamp"].dt.dayofweek

# --------------------------
# Remove rows with NaN
# --------------------------

df = df.dropna()

# --------------------------
# Save Features
# --------------------------

df.to_sql(

    "weather_features",

    engine,

    if_exists="replace",

    index=False

)

print("Feature table created successfully.")

print(df)