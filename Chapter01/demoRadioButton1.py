# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoRadioButton1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(470, 290)
        self.radioButtonBusinessClass = QtWidgets.QRadioButton(Dialog)
        self.radioButtonBusinessClass.setGeometry(QtCore.QRect(30, 130, 251, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButtonBusinessClass.setFont(font)
        self.radioButtonBusinessClass.setObjectName("radioButtonBusinessClass")
        self.radioButtonEconomyClass = QtWidgets.QRadioButton(Dialog)
        self.radioButtonEconomyClass.setGeometry(QtCore.QRect(30, 180, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButtonEconomyClass.setFont(font)
        self.radioButtonEconomyClass.setObjectName("radioButtonEconomyClass")
        self.radioButtonFirstClass = QtWidgets.QRadioButton(Dialog)
        self.radioButtonFirstClass.setGeometry(QtCore.QRect(30, 80, 201, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButtonFirstClass.setFont(font)
        self.radioButtonFirstClass.setObjectName("radioButtonFirstClass")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 10, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.labelFare = QtWidgets.QLabel(Dialog)
        self.labelFare.setGeometry(QtCore.QRect(40, 245, 391, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelFare.setFont(font)
        self.labelFare.setText("")
        self.labelFare.setObjectName("labelFare")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.radioButtonBusinessClass.setText(_translate("Dialog", "Business Class $125"))
        self.radioButtonEconomyClass.setText(_translate("Dialog", "Economy Class $100"))
        self.radioButtonFirstClass.setText(_translate("Dialog", "First Class   $150"))
        self.label.setText(_translate("Dialog", "Choose the flight type"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

