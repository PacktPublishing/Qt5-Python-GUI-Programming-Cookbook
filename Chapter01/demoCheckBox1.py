# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCheckBox1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(503, 272)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 0, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.checkBoxCheese = QtWidgets.QCheckBox(Dialog)
        self.checkBoxCheese.setGeometry(QtCore.QRect(270, 60, 191, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBoxCheese.setFont(font)
        self.checkBoxCheese.setObjectName("checkBoxCheese")
        self.checkBoxOlives = QtWidgets.QCheckBox(Dialog)
        self.checkBoxOlives.setGeometry(QtCore.QRect(270, 90, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBoxOlives.setFont(font)
        self.checkBoxOlives.setObjectName("checkBoxOlives")
        self.checkBoxSausages = QtWidgets.QCheckBox(Dialog)
        self.checkBoxSausages.setGeometry(QtCore.QRect(270, 120, 231, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBoxSausages.setFont(font)
        self.checkBoxSausages.setObjectName("checkBoxSausages")
        self.labelAmount = QtWidgets.QLabel(Dialog)
        self.labelAmount.setGeometry(QtCore.QRect(50, 190, 371, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAmount.setFont(font)
        self.labelAmount.setObjectName("labelAmount")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Regular Pizza   $10"))
        self.label_2.setText(_translate("Dialog", "Select your extra toppings"))
        self.checkBoxCheese.setText(_translate("Dialog", "Extra Cheese   $1"))
        self.checkBoxOlives.setText(_translate("Dialog", "Extra Olives $1"))
        self.checkBoxSausages.setText(_translate("Dialog", "Extra Sausages $2"))
        self.labelAmount.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

