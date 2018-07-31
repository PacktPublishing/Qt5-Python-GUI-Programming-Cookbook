# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoListWidget1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(686, 287)
        self.listWidgetDiagnosis = QtWidgets.QListWidget(Dialog)
        self.listWidgetDiagnosis.setGeometry(QtCore.QRect(280, 20, 351, 171))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidgetDiagnosis.setFont(font)
        self.listWidgetDiagnosis.setObjectName("listWidgetDiagnosis")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        self.labelTest = QtWidgets.QLabel(Dialog)
        self.labelTest.setGeometry(QtCore.QRect(40, 230, 621, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelTest.setFont(font)
        self.labelTest.setText("")
        self.labelTest.setObjectName("labelTest")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.listWidgetDiagnosis.isSortingEnabled()
        self.listWidgetDiagnosis.setSortingEnabled(False)
        item = self.listWidgetDiagnosis.item(0)
        item.setText(_translate("Dialog", "Urine Analaysis   $5"))
        item = self.listWidgetDiagnosis.item(1)
        item.setText(_translate("Dialog", "Chest X Ray 100$"))
        item = self.listWidgetDiagnosis.item(2)
        item.setText(_translate("Dialog", "Sugar Level test  $3"))
        item = self.listWidgetDiagnosis.item(3)
        item.setText(_translate("Dialog", "Hemoglobin test  $7"))
        item = self.listWidgetDiagnosis.item(4)
        item.setText(_translate("Dialog", "Thyroid Stimulating Harmone test   $10"))
        self.listWidgetDiagnosis.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Dialog", "Choose the Diagnosis Tests"))

