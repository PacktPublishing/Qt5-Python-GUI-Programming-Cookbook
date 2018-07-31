# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoSpinBox.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(580, 162)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(16, 30, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditBookPrice = QtWidgets.QLineEdit(Dialog)
        self.lineEditBookPrice.setGeometry(QtCore.QRect(120, 30, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditBookPrice.setFont(font)
        self.lineEditBookPrice.setObjectName("lineEditBookPrice")
        self.spinBoxBookQty = QtWidgets.QSpinBox(Dialog)
        self.spinBoxBookQty.setGeometry(QtCore.QRect(290, 30, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBoxBookQty.setFont(font)
        self.spinBoxBookQty.setObjectName("spinBoxBookQty")
        self.lineEditBookAmount = QtWidgets.QLineEdit(Dialog)
        self.lineEditBookAmount.setGeometry(QtCore.QRect(390, 30, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditBookAmount.setFont(font)
        self.lineEditBookAmount.setObjectName("lineEditBookAmount")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditSugarPrice = QtWidgets.QLineEdit(Dialog)
        self.lineEditSugarPrice.setGeometry(QtCore.QRect(120, 70, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditSugarPrice.setFont(font)
        self.lineEditSugarPrice.setObjectName("lineEditSugarPrice")
        self.doubleSpinBoxSugarWeight = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBoxSugarWeight.setGeometry(QtCore.QRect(290, 70, 62, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBoxSugarWeight.setFont(font)
        self.doubleSpinBoxSugarWeight.setObjectName("doubleSpinBoxSugarWeight")
        self.lineEditSugarAmount = QtWidgets.QLineEdit(Dialog)
        self.lineEditSugarAmount.setGeometry(QtCore.QRect(390, 70, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditSugarAmount.setFont(font)
        self.lineEditSugarAmount.setObjectName("lineEditSugarAmount")
        self.labelTotalAmount = QtWidgets.QLabel(Dialog)
        self.labelTotalAmount.setGeometry(QtCore.QRect(396, 120, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelTotalAmount.setFont(font)
        self.labelTotalAmount.setObjectName("labelTotalAmount")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Book Price"))
        self.label_2.setText(_translate("Dialog", "Sugar Price"))
        self.labelTotalAmount.setText(_translate("Dialog", "TextLabel"))

