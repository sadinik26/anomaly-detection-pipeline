import requests
from datetime import datetime
from sqlalchemy import create_engine, text

DATABASE_URL = "sqlite:///anomalies.db"

engine = create_engine(DATABASE_URL)

URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=6.9271"
    "&longitude=79.8612"
    "&current=temperature_2m"
)


def fetch_weather_data():

    response = requests.get(URL)

    if response.status_code != 200:
        print("Weather API Error")
        return

    data = response.json()

    temperature = data["current"]["temperature_2m"]

    timestamp = datetime.now()

    with engine.connect() as conn:

        conn.execute(
            text("""
            INSERT INTO weather_data
            (timestamp, temperature)
            VALUES
            (:timestamp, :temperature)
            """),
            {
                "timestamp": timestamp,
                "temperature": temperature
            }
        )

        conn.commit()

    print(
        f"[{timestamp}] Stored Temperature = {temperature}°C"
    )


if __name__ == "__main__":
    fetch_weather_data()