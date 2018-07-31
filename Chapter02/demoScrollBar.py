# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoScrollBar.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(538, 431)
        self.horizontalScrollBarSugarLevel = QtWidgets.QScrollBar(Dialog)
        self.horizontalScrollBarSugarLevel.setGeometry(QtCore.QRect(200, 30, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.horizontalScrollBarSugarLevel.setFont(font)
        self.horizontalScrollBarSugarLevel.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBarSugarLevel.setObjectName("horizontalScrollBarSugarLevel")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalScrollBarPulseRate = QtWidgets.QScrollBar(Dialog)
        self.verticalScrollBarPulseRate.setGeometry(QtCore.QRect(160, 110, 16, 160))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.verticalScrollBarPulseRate.setFont(font)
        self.verticalScrollBarPulseRate.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBarPulseRate.setObjectName("verticalScrollBarPulseRate")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 70, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalSliderBloodPressure = QtWidgets.QSlider(Dialog)
        self.horizontalSliderBloodPressure.setGeometry(QtCore.QRect(210, 70, 291, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.horizontalSliderBloodPressure.setFont(font)
        self.horizontalSliderBloodPressure.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderBloodPressure.setObjectName("horizontalSliderBloodPressure")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(240, 110, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalSliderCholestrolLevel = QtWidgets.QSlider(Dialog)
        self.verticalSliderCholestrolLevel.setGeometry(QtCore.QRect(410, 109, 22, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.verticalSliderCholestrolLevel.setFont(font)
        self.verticalSliderCholestrolLevel.setOrientation(QtCore.Qt.Vertical)
        self.verticalSliderCholestrolLevel.setObjectName("verticalSliderCholestrolLevel")
        self.lineEditResult = QtWidgets.QLineEdit(Dialog)
        self.lineEditResult.setGeometry(QtCore.QRect(60, 340, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditResult.setFont(font)
        self.lineEditResult.setObjectName("lineEditResult")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Sugar Level"))
        self.label_2.setText(_translate("Dialog", "Pulse rate"))
        self.label_3.setText(_translate("Dialog", "Blood Pressure"))
        self.label_4.setText(_translate("Dialog", "Cholestrol Level"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

