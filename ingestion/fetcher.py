import requests
import pandas as pd
from datetime import datetime

URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=6.9271"
    "&longitude=79.8612"
    "&current=temperature_2m"
)

response = requests.get(URL)

data = response.json()

temperature = data["current"]["temperature_2m"]

record = pd.DataFrame(
    [{
        "timestamp": datetime.now(),
        "temperature": temperature
    }]
)

print(record)