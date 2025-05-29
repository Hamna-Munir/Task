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

# Get UK Weather Details
city = "London"
api_key = "6210add1ec26099e556cb0c5f1197044"  # Your working API key
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url).json()

if response.get("main") and response.get("weather"):
    uk_temp = response["main"]["temp"]
    uk_humidity = response["main"]["humidity"]
    weather_desc = response["weather"][0]["description"].capitalize()
    print(f"UK Temperature in {city}: {uk_temp}°C")
    print(f"Weather: {weather_desc}")
    print(f"Humidity: {uk_humidity}%")
else:
    # fallback values
    uk_temp = 18
    weather_desc = "Unknown"
    uk_humidity = "N/A"
    print("❌ Could not fetch UK weather details.")

# Timer - user input for seconds
try:
    timer_seconds = int(input("Enter timer duration in seconds: "))
except ValueError:
    timer_seconds = 5  # default to 5 seconds if invalid input
print(f"Starting {timer_seconds} second timer...")
time.sleep(timer_seconds)
print("Time's up!")

# Toast Notification
notification.notify(
    title="UK Weather & Timer",
    message=f"UK Temp: {uk_temp}°C, {weather_desc}\nTimer for {timer_seconds} seconds finished!",
    timeout=5
)
