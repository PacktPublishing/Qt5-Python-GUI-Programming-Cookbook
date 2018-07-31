# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoListWidgetOp.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(691, 260)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(16, 30, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 30, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButtonAdd = QtWidgets.QPushButton(Dialog)
        self.pushButtonAdd.setGeometry(QtCore.QRect(180, 80, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonAdd.setFont(font)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(380, 30, 256, 192))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.pushButtonDelete = QtWidgets.QPushButton(Dialog)
        self.pushButtonDelete.setGeometry(QtCore.QRect(470, 230, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonDelete.setFont(font)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.pushButtonDeleteAll = QtWidgets.QPushButton(Dialog)
        self.pushButtonDeleteAll.setGeometry(QtCore.QRect(560, 230, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonDeleteAll.setFont(font)
        self.pushButtonDeleteAll.setObjectName("pushButtonDeleteAll")
        self.pushButtonEdit = QtWidgets.QPushButton(Dialog)
        self.pushButtonEdit.setGeometry(QtCore.QRect(380, 230, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonEdit.setFont(font)
        self.pushButtonEdit.setObjectName("pushButtonEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter an item"))
        self.pushButtonAdd.setText(_translate("Dialog", "Add"))
        self.pushButtonDelete.setText(_translate("Dialog", "Delete"))
        self.pushButtonDeleteAll.setText(_translate("Dialog", "Delete All"))
        self.pushButtonEdit.setText(_translate("Dialog", "Edit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

