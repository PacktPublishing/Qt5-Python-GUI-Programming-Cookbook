# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reservehotel.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(553, 556)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 10, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 250, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(210, 60, 312, 183))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setObjectName("calendarWidget")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(210, 260, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 300, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(210, 300, 211, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 350, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.Enteredinfo = QtWidgets.QLabel(Dialog)
        self.Enteredinfo.setGeometry(QtCore.QRect(20, 400, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Enteredinfo.setFont(font)
        self.Enteredinfo.setText("")
        self.Enteredinfo.setObjectName("Enteredinfo")
        self.RoomRentinfo = QtWidgets.QLabel(Dialog)
        self.RoomRentinfo.setGeometry(QtCore.QRect(10, 480, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RoomRentinfo.setFont(font)
        self.RoomRentinfo.setText("")
        self.RoomRentinfo.setObjectName("RoomRentinfo")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Hotel Room Reservation"))
        self.label_2.setText(_translate("Dialog", "Date of Reservation"))
        self.label_3.setText(_translate("Dialog", "Number of days"))
        self.label_4.setText(_translate("Dialog", "Room type"))
        self.pushButton.setText(_translate("Dialog", "Caclulate Room Rent"))

