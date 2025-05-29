from PyQt5 import QtCore, QtWidgets

class Ui_Form2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 300)

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

        # Photo Upload
        self.label_photo = QtWidgets.QLabel("Upload Photo:")
        self.gridLayout.addWidget(self.label_photo, 3, 0)
        self.lineEdit_photo = QtWidgets.QLineEdit()
        self.lineEdit_photo.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_photo, 3, 1)
        self.btn_browse = QtWidgets.QPushButton("Browse")
        self.gridLayout.addWidget(self.btn_browse, 3, 2)

        # Submit Button
        self.pushButton_submit = QtWidgets.QPushButton("Submit")
        self.gridLayout.addWidget(self.pushButton_submit, 4, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Form 2 - Upload Photo"))
