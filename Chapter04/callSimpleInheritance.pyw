import sys

from PyQt5.QtWidgets import QDialog, QApplication

from demoSimpleInheritance import *

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


class Marks(Student):
    historyMarks = 0
    geographyMarks = 0
 
    def __init__(self,  code, name, historyMarks, geographyMarks):
        Student.__init__(self,code,name)
        self.historyMarks = historyMarks
        self.geographyMarks = geographyMarks
        
    def getHistoryMarks(self):
        return self.historyMarks

    def getGeographyMarks(self):
        return self.geographyMarks
    

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ButtonClickMe.clicked.connect(self.dispmessage)
        self.show()

    def dispmessage(self):
        marksObj=Marks(self.ui.lineEditCode.text(), self.ui.lineEditName.text(), self.ui.lineEditHistoryMarks.text(), self.ui.lineEditGeographyMarks.text())  
        self.ui.labelResponse.setText("Code: "+marksObj.getCode()+", Name:"+marksObj.getName()+"\nHistory Marks:"+marksObj.getHistoryMarks()+", Geography Marks:"+marksObj.getGeographyMarks())

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
