# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCalculator.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(427, 269)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditFirstNumber = QtWidgets.QLineEdit(Dialog)
        self.lineEditFirstNumber.setGeometry(QtCore.QRect(180, 30, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditFirstNumber.setFont(font)
        self.lineEditFirstNumber.setObjectName("lineEditFirstNumber")
        self.lineEditSecondNumber = QtWidgets.QLineEdit(Dialog)
        self.lineEditSecondNumber.setGeometry(QtCore.QRect(180, 80, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditSecondNumber.setFont(font)
        self.lineEditSecondNumber.setObjectName("lineEditSecondNumber")
        self.pushButtonPlus = QtWidgets.QPushButton(Dialog)
        self.pushButtonPlus.setGeometry(QtCore.QRect(20, 150, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonPlus.setFont(font)
        self.pushButtonPlus.setObjectName("pushButtonPlus")
        self.pushButtonSubtract = QtWidgets.QPushButton(Dialog)
        self.pushButtonSubtract.setGeometry(QtCore.QRect(120, 150, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSubtract.setFont(font)
        self.pushButtonSubtract.setObjectName("pushButtonSubtract")
        self.pushButtonMultiply = QtWidgets.QPushButton(Dialog)
        self.pushButtonMultiply.setGeometry(QtCore.QRect(220, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonMultiply.setFont(font)
        self.pushButtonMultiply.setObjectName("pushButtonMultiply")
        self.pushButtonDivide = QtWidgets.QPushButton(Dialog)
        self.pushButtonDivide.setGeometry(QtCore.QRect(330, 150, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonDivide.setFont(font)
        self.pushButtonDivide.setObjectName("pushButtonDivide")
        self.labelResult = QtWidgets.QLabel(Dialog)
        self.labelResult.setGeometry(QtCore.QRect(30, 210, 351, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelResult.setFont(font)
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter first number"))
        self.label_2.setText(_translate("Dialog", "Enter second number"))
        self.pushButtonPlus.setText(_translate("Dialog", "+"))
        self.pushButtonSubtract.setText(_translate("Dialog", "-"))
        self.pushButtonMultiply.setText(_translate("Dialog", "X"))
        self.pushButtonDivide.setText(_translate("Dialog", "/"))

