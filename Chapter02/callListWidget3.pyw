import sys

from PyQt5.QtWidgets import QDialog, QApplication

from demoListWidget3 import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonAdd.clicked.connect(self.addlist)
        self.show()

    def addlist(self):
        self.ui.listWidgetSelectedItems.addItem(self.ui.lineEditFoodItem.text())
        self.ui.lineEditFoodItem.setText('')
        self.ui.lineEditFoodItem.setFocus()
        
if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
