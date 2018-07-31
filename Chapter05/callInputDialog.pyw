import sys

from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog

from demoInputDialog import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonCountry.clicked.connect(self.dispmessage)
        self.show()

    def dispmessage(self):
      countries = ("Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan")
      countryName, ok = QInputDialog.getItem(self, "Input Dialog", "List of countries", countries, 0, False)			
      if ok and countryName:
          self.ui.lineEditCountry.setText(countryName)

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())

