# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoListWidget3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(734, 270)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditFoodItem = QtWidgets.QLineEdit(Dialog)
        self.lineEditFoodItem.setGeometry(QtCore.QRect(210, 20, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditFoodItem.setFont(font)
        self.lineEditFoodItem.setObjectName("lineEditFoodItem")
        self.pushButtonAdd = QtWidgets.QPushButton(Dialog)
        self.pushButtonAdd.setGeometry(QtCore.QRect(110, 72, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonAdd.setFont(font)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.listWidgetSelectedItems = QtWidgets.QListWidget(Dialog)
        self.listWidgetSelectedItems.setGeometry(QtCore.QRect(430, 20, 256, 221))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidgetSelectedItems.setFont(font)
        self.listWidgetSelectedItems.setObjectName("listWidgetSelectedItems")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Your favourite food item"))
        self.pushButtonAdd.setText(_translate("Dialog", "Add to List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

