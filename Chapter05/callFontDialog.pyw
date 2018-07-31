import sys

from PyQt5.QtWidgets import QDialog, QApplication, QFontDialog


from demoFontDialog import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)      
        self.ui.pushButtonFont.clicked.connect(self.changefont)
        self.show()

    def changefont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.ui.textEdit.setFont(font)

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())

