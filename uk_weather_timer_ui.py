import sys
import datetime
import pytz
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
)
from PyQt5.QtCore import QTimer
from plyer import notification

class WeatherTimerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.timer_seconds = 0
        self.countdown_timer = QTimer()
        self.countdown_timer.timeout.connect(self.update_countdown)

    def initUI(self):
        self.setWindowTitle("UK Weather & Timer")

        self.uk_time_label = QLabel("UK Time: Loading...")
        self.local_time_label = QLabel("Local Time: Loading...")
        self.temp_label = QLabel("Temperature: Loading...")
        self.weather_label = QLabel("Weather: Loading...")
        self.humidity_label = QLabel("Humidity: Loading...")

        self.timer_input = QLineEdit()
        self.timer_input.setPlaceholderText("Enter timer in seconds")

        self.start_button = QPushButton("Start Timer")
        self.start_button.clicked.connect(self.start_timer)

        self.countdown_label = QLabel("Timer not started")

        layout = QVBoxLayout()
        layout.addWidget(self.uk_time_label)
        layout.addWidget(self.local_time_label)
        layout.addWidget(self.temp_label)
        layout.addWidget(self.weather_label)
        layout.addWidget(self.humidity_label)
        layout.addWidget(self.timer_input)
        layout.addWidget(self.start_button)
        layout.addWidget(self.countdown_label)

        self.setLayout(layout)

        self.fetch_weather_and_time()

    def fetch_weather_and_time(self):
        # UK Time
        uk_timezone = pytz.timezone("Europe/London")
        uk_time = datetime.datetime.now(uk_timezone)
        self.uk_time_label.setText(f"UK Time: {uk_time.strftime('%Y-%m-%d %H:%M:%S')}")

        # Local Time
        local_time = datetime.datetime.now()
        self.local_time_label.setText(f"Local Time: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")

        # Fetch weather from API
        city = "London"
        api_key = "2115eb1f7a50543b04d97e25ce9b5453"  # Replace with your API key
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url).json()

        if response.get("main") and response.get("weather"):
            uk_temp = response["main"]["temp"]
            uk_humidity = response["main"]["humidity"]
            weather_desc = response["weather"][0]["description"].capitalize()
            self.temp_label.setText(f"Temperature: {uk_temp}°C")
            self.weather_label.setText(f"Weather: {weather_desc}")
            self.humidity_label.setText(f"Humidity: {uk_humidity}%")
            self.uk_temp = uk_temp
            self.weather_desc = weather_desc
        else:
            self.temp_label.setText("Temperature: N/A")
            self.weather_label.setText("Weather: N/A")
            self.humidity_label.setText("Humidity: N/A")
            self.uk_temp = "N/A"
            self.weather_desc = "N/A"

    def start_timer(self):
        try:
            self.timer_seconds = int(self.timer_input.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid input", "Please enter a valid integer for seconds.")
            return

        if self.timer_seconds <= 0:
            QMessageBox.warning(self, "Invalid input", "Timer must be greater than zero.")
            return

        self.countdown_label.setText(f"Time left: {self.timer_seconds} seconds")
        self.countdown_timer.start(1000)  # Tick every 1 second

    def update_countdown(self):
        self.timer_seconds -= 1
        if self.timer_seconds > 0:
            self.countdown_label.setText(f"Time left: {self.timer_seconds} seconds")
        else:
            self.countdown_timer.stop()
            self.countdown_label.setText("Time's up!")

            # Show notification
            notification.notify(
                title="UK Weather & Timer",
                message=f"Timer finished!\nUK Temp: {self.uk_temp}°C, {self.weather_desc}",
                timeout=5
            )

app = QApplication(sys.argv)
window = WeatherTimerApp()
window.show()
sys.exit(app.exec_())
