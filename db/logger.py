from sqlalchemy import create_engine, text

DATABASE_URL = "sqlite:///anomalies.db"

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:

    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS weather_data (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp DATETIME NOT NULL,

            temperature REAL NOT NULL

        );
    """))

    conn.commit()

print("Database and weather_data table created successfully.")