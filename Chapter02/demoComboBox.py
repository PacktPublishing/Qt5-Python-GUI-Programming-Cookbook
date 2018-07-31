# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoComboBox.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(674, 200)
        self.comboBoxAccountType = QtWidgets.QComboBox(Dialog)
        self.comboBoxAccountType.setGeometry(QtCore.QRect(260, 40, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBoxAccountType.setFont(font)
        self.comboBoxAccountType.setObjectName("comboBoxAccountType")
        self.comboBoxAccountType.addItem("")
        self.comboBoxAccountType.addItem("")
        self.comboBoxAccountType.addItem("")
        self.comboBoxAccountType.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.labelAccountType = QtWidgets.QLabel(Dialog)
        self.labelAccountType.setGeometry(QtCore.QRect(40, 110, 581, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAccountType.setFont(font)
        self.labelAccountType.setText("")
        self.labelAccountType.setObjectName("labelAccountType")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBoxAccountType.setItemText(0, _translate("Dialog", "Saving Account"))
        self.comboBoxAccountType.setItemText(1, _translate("Dialog", "Current Account"))
        self.comboBoxAccountType.setItemText(2, _translate("Dialog", "Recurring Deposit Account"))
        self.comboBoxAccountType.setItemText(3, _translate("Dialog", "Fixed Deposit Account"))
        self.label.setText(_translate("Dialog", "Select your account type"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

