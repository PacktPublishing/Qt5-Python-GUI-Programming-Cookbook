# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoBrowser.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(563, 339)
        self.widget = QWebEngineView(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 60, 531, 251))
        self.widget.setObjectName("widget")
        self.pushButtonGo = QtWidgets.QPushButton(Dialog)
        self.pushButtonGo.setGeometry(QtCore.QRect(450, 20, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonGo.setFont(font)
        self.pushButtonGo.setObjectName("pushButtonGo")
        self.lineEditURL = QtWidgets.QLineEdit(Dialog)
        self.lineEditURL.setGeometry(QtCore.QRect(100, 20, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditURL.setFont(font)
        self.lineEditURL.setObjectName("lineEditURL")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonGo.setText(_translate("Dialog", "Go"))
        self.label.setText(_translate("Dialog", "Enter URL"))

from PyQt5.QtWebEngineWidgets import QWebEngineView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

