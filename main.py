import sys
import sqlite3
from PyQt5 import QtWidgets
from form1 import Ui_Dialog  # form1.py must be in the same folder

class MyApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Connect Save button
        self.ui.pushButton.clicked.connect(self.save_data)

        # Create database table if not exists
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect("userdata.db")
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                email TEXT,
                gender TEXT
            )
        """)
        conn.commit()
        conn.close()

    def save_data(self):
        first = self.ui.lineEdit_first.text()
        last = self.ui.lineEdit_last.text()
        email = self.ui.lineEdit_email.text()
        gender = self.ui.comboBox.currentText()

        if first and last and email:
            conn = sqlite3.connect("userdata.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO users (first_name, last_name, email, gender) VALUES (?, ?, ?, ?)",
                        (first, last, email, gender))
            conn.commit()
            conn.close()
            QtWidgets.QMessageBox.information(self, "Success", "Data saved successfully!")
            self.clear_fields()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Please fill all the fields.")

    def clear_fields(self):
        self.ui.lineEdit_first.clear()
        self.ui.lineEdit_last.clear()
        self.ui.lineEdit_email.clear()
        self.ui.comboBox.setCurrentIndex(0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

