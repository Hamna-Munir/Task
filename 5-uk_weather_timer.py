import datetime
import pytz
import requests
from plyer import notification
import time

# UK Time
uk_timezone = pytz.timezone("Europe/London")
uk_time = datetime.datetime.now(uk_timezone)
print("UK Time:", uk_time.strftime("%Y-%m-%d %H:%M:%S"))

# Local Time
local_time = datetime.datetime.now()
print("Local Time:", local_time.strftime("%Y-%m-%d %H:%M:%S"))

# Get UK Temperature
city = "London"
api_key = "6210add1ec26099e556cb0c5f1197044"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url).json()

if response.get("main"):
    uk_temp = response["main"]["temp"]
    print(f"UK Temperature in {city}: {uk_temp}°C")
else:
    print("❌ Could not fetch UK temperature. Check API key or connection.")

# Timer
print("Starting 5 second timer...")
time.sleep(5)
print("Time's up!")

# Toast Notification
notification.notify(
    title="Reminder",
    message="This is your toast notification!",
    timeout=5
)

