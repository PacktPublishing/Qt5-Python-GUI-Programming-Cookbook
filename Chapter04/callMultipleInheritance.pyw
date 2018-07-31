import sys

from PyQt5.QtWidgets import QDialog, QApplication

from demoMultipleInheritance import *

class Student:
    name = ""
    code = ""
 
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def getCode(self):
        return self.code
    
    def getName(self):
        return self.name


class Marks:
    historyMarks = 0
    geographyMarks = 0
 
    def __init__(self,  historyMarks, geographyMarks):
        self.historyMarks = historyMarks
        self.geographyMarks = geographyMarks
        
    def getHistoryMarks(self):
        return self.historyMarks

    def getGeographyMarks(self):
        return self.geographyMarks

class Result(Student, Marks):
    totalMarks = 0
    percentage = 0
 
    def __init__(self,  code, name, historyMarks, geographyMarks):
        Student.__init__(self,  code, name)
        Marks.__init__(self, historyMarks, geographyMarks)
        self.totalMarks = historyMarks + geographyMarks
        self.percentage = (historyMarks + geographyMarks) / 200 * 100
        
    def getTotalMarks(self):
        return self.totalMarks

    def getPercentage(self):
        return self.percentage

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ButtonClickMe.clicked.connect(self.dispmessage)
        self.show()

    def dispmessage(self):
        resultObj=Result(self.ui.lineEditCode.text(), self.ui.lineEditName.text(), int(self.ui.lineEditHistoryMarks.text()), int(self.ui.lineEditGeographyMarks.text()))
        self.ui.lineEditTotal.setText(str(resultObj.getTotalMarks()))
        self.ui.lineEditPercentage.setText(str(resultObj.getPercentage()))      

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
