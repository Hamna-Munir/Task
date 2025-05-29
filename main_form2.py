import sys
import os
import shutil
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from form2 import Ui_Form2  # Make sure form2.py is in the same folder

class Form2App(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form2()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.btn_browse.clicked.connect(self.browse_photo)
        self.ui.pushButton_submit.clicked.connect(self.submit_form)

        # Create table if not exists
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect("form2data.db")
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                email TEXT,
                photo TEXT
            )
        """)
        conn.commit()
        conn.close()

    def browse_photo(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Photo", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.ui.lineEdit_photo.setText(file_path)

    def submit_form(self):
        first = self.ui.lineEdit_first.text()
        last = self.ui.lineEdit_last.text()
        email = self.ui.lineEdit_email.text()
        photo_path = self.ui.lineEdit_photo.text()

        if first and last and email and photo_path:
            # Optional: Copy photo to /photos directory
            os.makedirs("photos", exist_ok=True)
            photo_filename = os.path.basename(photo_path)
            saved_path = os.path.join("photos", photo_filename)
            shutil.copy(photo_path, saved_path)

            # Save to database
            conn = sqlite3.connect("form2data.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO users (first_name, last_name, email, photo) VALUES (?, ?, ?, ?)",
                        (first, last, email, saved_path))
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Success", "User data saved successfully!")
            self.clear_form()
        else:
            QMessageBox.warning(self, "Error", "Please fill all fields and upload a photo.")

    def clear_form(self):
        self.ui.lineEdit_first.clear()
        self.ui.lineEdit_last.clear()
        self.ui.lineEdit_email.clear()
        self.ui.lineEdit_photo.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Form2App()
    window.show()
    sys.exit(app.exec_())
