# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoColorDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 176)
        self.frameColor = QtWidgets.QFrame(Dialog)
        self.frameColor.setGeometry(QtCore.QRect(210, 20, 120, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frameColor.setFont(font)
        self.frameColor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameColor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameColor.setObjectName("frameColor")
        self.pushButtonColor = QtWidgets.QPushButton(Dialog)
        self.pushButtonColor.setGeometry(QtCore.QRect(30, 40, 151, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonColor.setFont(font)
        self.pushButtonColor.setObjectName("pushButtonColor")
        self.labelColor = QtWidgets.QLabel(Dialog)
        self.labelColor.setGeometry(QtCore.QRect(30, 130, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelColor.setFont(font)
        self.labelColor.setText("")
        self.labelColor.setObjectName("labelColor")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonColor.setText(_translate("Dialog", "Choose color"))

