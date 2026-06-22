from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///anomalies.db"

engine = create_engine(DATABASE_URL)

print("Database initialized successfully")