# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoFontDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(30, 60, 331, 221))
        self.textEdit.setObjectName("textEdit")
        self.pushButtonFont = QtWidgets.QPushButton(Dialog)
        self.pushButtonFont.setGeometry(QtCore.QRect(120, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonFont.setFont(font)
        self.pushButtonFont.setObjectName("pushButtonFont")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonFont.setText(_translate("Dialog", "Change Font"))

