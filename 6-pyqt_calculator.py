from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Calculator")
        self.setGeometry(100, 100, 300, 200)
        self.layout = QVBoxLayout()

        self.input = QLineEdit(self)
        self.layout.addWidget(self.input)

        self.button = QPushButton("Calculate", self)
        self.button.clicked.connect(self.calculate)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def calculate(self):
        try:
            result = eval(self.input.text())
            self.input.setText(str(result))
        except:
            self.input.setText("Error")

app = QApplication(sys.argv)
win = Calculator()
win.show()
sys.exit(app.exec_())

