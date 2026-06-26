from apscheduler.schedulers.blocking import BlockingScheduler
from fetcher import fetch_weather_data

scheduler = BlockingScheduler()

scheduler.add_job(
    fetch_weather_data,
    trigger="interval",
    minutes=5,
    id="weather_fetch_job",
    replace_existing=True
)

print("=" * 60)
print(" Weather Scheduler Started")
print(" Fetching weather every 5 minutes")
print(" Press CTRL + C to stop")
print("=" * 60)

fetch_weather_data()

scheduler.start()