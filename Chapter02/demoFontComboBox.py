# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoFontComboBox.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(560, 228)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.labelTextLine = QtWidgets.QLabel(Dialog)
        self.labelTextLine.setGeometry(QtCore.QRect(20, 60, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelTextLine.setFont(font)
        self.labelTextLine.setObjectName("labelTextLine")
        self.fontComboBox = QtWidgets.QFontComboBox(Dialog)
        self.fontComboBox.setGeometry(QtCore.QRect(200, 20, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fontComboBox.setFont(font)
        self.fontComboBox.setObjectName("fontComboBox")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(200, 70, 321, 121))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select desired font"))
        self.labelTextLine.setText(_translate("Dialog", "Type some text"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

