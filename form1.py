from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 250)

        # Create layout
        self.gridLayout = QtWidgets.QGridLayout(Dialog)

        # First Name
        self.label_first = QtWidgets.QLabel("First Name:")
        self.gridLayout.addWidget(self.label_first, 0, 0)
        self.lineEdit_first = QtWidgets.QLineEdit()
        self.gridLayout.addWidget(self.lineEdit_first, 0, 1)

        # Last Name
        self.label_last = QtWidgets.QLabel("Last Name:")
        self.gridLayout.addWidget(self.label_last, 1, 0)
        self.lineEdit_last = QtWidgets.QLineEdit()
        self.gridLayout.addWidget(self.lineEdit_last, 1, 1)

        # Email
        self.label_email = QtWidgets.QLabel("Email:")
        self.gridLayout.addWidget(self.label_email, 2, 0)
        self.lineEdit_email = QtWidgets.QLineEdit()
        self.gridLayout.addWidget(self.lineEdit_email, 2, 1)

        # Gender
        self.label_gender = QtWidgets.QLabel("Gender:")
        self.gridLayout.addWidget(self.label_gender, 3, 0)
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItems(["Male", "Female", "Other"])
        self.gridLayout.addWidget(self.comboBox, 3, 1)

        # Save Button
        self.pushButton = QtWidgets.QPushButton("Save")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 2)

        # Optional: ButtonBox for OK/Cancel
        self.buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 2)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "User Form"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
