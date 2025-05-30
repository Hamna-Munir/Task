import sys
import cv2
import pyautogui
import datetime
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap

class CameraApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📸 Camera & Screenshot App")
        self.setGeometry(100, 100, 640, 520)

        self.image_label = QLabel(self)
        self.image_label.setFixedSize(640, 480)

        self.btn_capture = QPushButton("📷 Capture Photo")
        self.btn_screenshot = QPushButton("🖼️ Take Screenshot")
        self.btn_quit = QPushButton("❌ Quit")

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.btn_capture)
        layout.addWidget(self.btn_screenshot)
        layout.addWidget(self.btn_quit)
        self.setLayout(layout)

        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(20)

        self.btn_capture.clicked.connect(self.capture_photo)
        self.btn_screenshot.clicked.connect(self.take_screenshot)
        self.btn_quit.clicked.connect(self.close_app)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            self.last_frame = frame
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_frame.shape
            bytes_per_line = ch * w
            q_img = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.image_label.setPixmap(QPixmap.fromImage(q_img))

    def capture_photo(self):
        if hasattr(self, 'last_frame'):
            filename = f"webcam_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            cv2.imwrite(filename, self.last_frame)
            print(f"✅ Webcam photo saved as {filename}")

    def take_screenshot(self):
        screenshot = pyautogui.screenshot()
        filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        screenshot.save(filename)
        print(f"✅ Screenshot saved as {filename}")

    def close_app(self):
        self.cap.release()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CameraApp()
    window.show()
    sys.exit(app.exec_())
