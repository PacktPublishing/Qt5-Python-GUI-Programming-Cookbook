import sys

from PyQt5.QtWidgets import QDialog, QApplication

from demoComboBox import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.comboBoxAccountType.currentIndexChanged.connect(self.dispAccountType)
        self.show()

    def dispAccountType(self):
        self.ui.labelAccountType.setText("You have selected "+self.ui.comboBoxAccountType.itemText(self.ui.comboBoxAccountType.currentIndex()))

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
