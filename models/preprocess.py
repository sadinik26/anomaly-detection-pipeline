import joblib
import pandas as pd
from sqlalchemy import create_engine
from sklearn.preprocessing import StandardScaler

# -----------------------------
# Database Connection
# -----------------------------
DATABASE_URL = "sqlite:///anomalies.db"

engine = create_engine(DATABASE_URL)

# -----------------------------
# Load Feature Table
# -----------------------------
query = """
SELECT
temperature,
rolling_mean,
rolling_std,
lag_1,
hour,
day_of_week
FROM weather_features
"""

df = pd.read_sql(query, engine)

print("=" * 60)
print("Original Features")
print("=" * 60)
print(df)

# -----------------------------
# Scale Features
# -----------------------------
scaler = StandardScaler()

scaled_features = scaler.fit_transform(df)

scaled_df = pd.DataFrame(
    scaled_features,
    columns=df.columns
)

# -----------------------------
# Save Scaler
# -----------------------------
joblib.dump(
    scaler,
    "models/scaler.pkl"
)

print("\nScaler saved successfully!")

print("=" * 60)
print("Scaled Features")
print("=" * 60)
print(scaled_df)