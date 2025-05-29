import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from db_setup import init_db
from signup import SignupScreen
from login import LoginScreen
from calculator import CalculatorScreen

class App(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.signup_screen = SignupScreen(self.show_login)
        self.login_screen = LoginScreen(self.show_calculator)
        self.calculator_screen = CalculatorScreen()

        self.addWidget(self.signup_screen)
        self.addWidget(self.login_screen)
        self.addWidget(self.calculator_screen)

        self.setCurrentWidget(self.signup_screen)

    def show_login(self):
        self.setCurrentWidget(self.login_screen)

    def show_calculator(self):
        self.setCurrentWidget(self.calculator_screen)

if __name__ == "__main__":
    init_db()
    app = QApplication(sys.argv)
    window = App()
    window.setFixedSize(300, 400)
    window.show()
    sys.exit(app.exec_())
