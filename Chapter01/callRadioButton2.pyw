import sys

from PyQt5.QtWidgets import QDialog, QApplication

from demoRadioButton2 import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioButtonMedium.toggled.connect(self.dispSelected)
        self.ui.radioButtonLarge.toggled.connect(self.dispSelected)
        self.ui.radioButtonXL.toggled.connect(self.dispSelected)
        self.ui.radioButtonXXL.toggled.connect(self.dispSelected)
        self.ui.radioButtonDebitCard.toggled.connect(self.dispSelected)
        self.ui.radioButtonNetBanking.toggled.connect(self.dispSelected)
        self.ui.radioButtonCashOnDelivery.toggled.connect(self.dispSelected)
        self.show()

    def dispSelected(self):
        selected1="";
        selected2=""
        if self.ui.radioButtonMedium.isChecked()==True:
            selected1="Medium"
        if self.ui.radioButtonLarge.isChecked()==True:
            selected1="Large"
        if self.ui.radioButtonXL.isChecked()==True:
            selected1="Extra Large"
        if self.ui.radioButtonXXL.isChecked()==True:
            selected1="Extra Extra Large"
        if self.ui.radioButtonDebitCard.isChecked()==True:
            selected2="Debit/Credit Card"
        if self.ui.radioButtonNetBanking.isChecked()==True:
            selected2="NetBanking"
        if self.ui.radioButtonCashOnDelivery.isChecked()==True:
            selected2="Cash On Delivery"
        self.ui.labelSelected.setText("Chosen shirt size is "+selected1+" and payment method as " + selected2)

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
