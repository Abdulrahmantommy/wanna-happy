from PyQt5.QtGui import * # FOR NOTE OF ANY CHANGE
from PyQt5.QtCore import * # FOR NOTE OF ANY CHANGE
from PyQt5.QtWidgets import *  # FOR NOTE OF ANY CHANGE
from PyQt5.uic import loadUiType
import sys
from PyQt5.QtWidgets import *
ui, _ = loadUiType('EMC.ui')
class MainApp2(QMainWindow , ui): # Class Main
    def __init__(self, parent=None):
        super(MainApp2, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handel() # for any button
    def handel(self):
        self.pushButton_ok.clicked.connect(self.all)
    def all(self): # ECM
     try:
        density = float(self.lineEdit_density.text())
        atomic_weight = float(self.lineEdit_atomic_weight.text())
        valency = int(self.lineEdit_valency.text())
        material_removal_rate = float(self.lineEdit_Material_removal_rate.text())
        I =density*valency*material_removal_rate*96500/atomic_weight
        QMessageBox.information(self, "Final",
                            f"the current: {I} (Ampere)")

     except ValueError as e: # For error number (int) to float
         print(e)
         QMessageBox.information(self, "Error",
                            f"Please Enter Intger Number") # msgBoxError

    def finall(self): # for page 2
        pass
    def get_all(self): # for page 3 (with Data.txt)
        pass

def main(): # for Run App
            app = QApplication(sys.argv)
            window2 = MainApp2()
            window2.show()
            app.exec_()

if __name__ == '__main__':
    main() # for loop
