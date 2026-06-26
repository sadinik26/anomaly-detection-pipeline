from sqlalchemy import create_engine, text

DATABASE_URL = "sqlite:///anomalies.db"

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:

    conn.execute(text("""
    CREATE TABLE IF NOT EXISTS weather_data(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        timestamp DATETIME,

        temperature REAL

    );
    """))

    conn.execute(text("""
    CREATE TABLE IF NOT EXISTS weather_features(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        timestamp DATETIME,

        temperature REAL,

        rolling_mean REAL,

        rolling_std REAL,

        lag_1 REAL,

        hour INTEGER,

        day_of_week INTEGER

    );
    """))

    conn.commit()

print("Database initialized successfully.")