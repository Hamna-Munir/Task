import cv2
import pyautogui
import datetime

# Initialize webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Camera not found or cannot be opened.")
else:
    print("✅ Camera opened.")
    print("Type 's' to save a webcam picture.")
    print("Type 'p' to take a screenshot of the screen.")
    print("Type 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to grab frame from camera.")
            break

        key = input("\nYour choice (s/p/q): ").lower()

        if key == 's':
            filename = f"webcam_pic_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            cv2.imwrite(filename, frame)
            print(f"📷 Webcam picture saved as: {filename}")

        elif key == 'p':
            screenshot = pyautogui.screenshot()
            filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            screenshot.save(filename)
            print(f"🖼️ Screenshot saved as: {filename}")

        elif key == 'q':
            print("👋 Quitting the app.")
            break

cap.release()
