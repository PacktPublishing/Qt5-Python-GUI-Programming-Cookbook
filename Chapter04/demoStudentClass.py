# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoStudentClass.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(412, 208)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 60, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(30, 120, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelResponse.setFont(font)
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(140, 60, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditName.setFont(font)
        self.lineEditName.setObjectName("lineEditName")
        self.ButtonClickMe = QtWidgets.QPushButton(Dialog)
        self.ButtonClickMe.setGeometry(QtCore.QRect(140, 170, 101, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ButtonClickMe.setFont(font)
        self.ButtonClickMe.setObjectName("ButtonClickMe")
        self.lineEditCode = QtWidgets.QLineEdit(Dialog)
        self.lineEditCode.setGeometry(QtCore.QRect(140, 20, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditCode.setFont(font)
        self.lineEditCode.setObjectName("lineEditCode")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Student Name"))
        self.ButtonClickMe.setText(_translate("Dialog", "Click"))
        self.label_2.setText(_translate("Dialog", "Student Code"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

