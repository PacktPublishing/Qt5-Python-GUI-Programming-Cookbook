
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(565, 74)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditCountry = QtWidgets.QLineEdit(Dialog)
        self.lineEditCountry.setGeometry(QtCore.QRect(140, 20, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditCountry.setFont(font)
        self.lineEditCountry.setObjectName("lineEditCountry")
        self.pushButtonCountry = QtWidgets.QPushButton(Dialog)
        self.pushButtonCountry.setGeometry(QtCore.QRect(400, 20, 131, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonCountry.setFont(font)
        self.pushButtonCountry.setObjectName("pushButtonCountry")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Your Country:"))
        self.pushButtonCountry.setText(_translate("Dialog", "Choose Country"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

