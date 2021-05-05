from PyQt5.uic import loadUiType
import sys
from PyQt5.QtWidgets import *
ui, _ = loadUiType('EMC.ui')
class MainApp(QMainWindow, ui):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setFixedSize(809, 600)
        self.setupUi(self)
        self.handel()
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.tabBar().setVisible(False)
    def handel(self):
        self.pushButton_goto_ECMPAGE.clicked.connect(self.tap1)
        self.pushButton_EXIT.clicked.connect(self.tap0)
        self.pushButton_EXIT_2.clicked.connect(self.tap1)
        self.pushButton_EXIT_3.clicked.connect(self.tap2)
        self.pushButton_EXIT_4.clicked.connect(self.tap3)
        self.pushButton_ok.clicked.connect(self.mathematical1)
        self.pushButton_ok_8.clicked.connect(self.mathematical2)
        self.pushButton_ok_9.clicked.connect(self.mathematical3)
        self.pushButton_ok_10.clicked.connect(self.mathematical4)
    def mathematical1(self):
        try:
            self.density = float(self.lineEdit_density.text())
            self.atomic_weight = float(self.lineEdit_atomic_weight.text())
            self.valency = int(self.lineEdit_valency.text())
            self.FINAL_1 = (self.atomic_weight * 60 * 1000) / (self.valency * self.density * 96500)
            self.tabWidget.setCurrentIndex(2)
            self.li = [self.textEdit, self.textEdit_2, self.textEdit_3, self.textEdit_4]
            for i in self.li:
                i.setPlainText(f'''Density = {self.density} gm/cm³
Atomic Weight = {self.atomic_weight} g/mole 
Valency = {self.valency}
MRR = {float(round(self.FINAL_1, 3))} mm³/A.min
************************''')
            return self.FINAL_1
        except ValueError as e:
            print(e)
            QMessageBox.information(self, "Error", f"{e}")
    def mathematical2(self):
        try:
            self.Working_Area = float(self.lineEdit_Working_Area.text())
            self.rate_of_feed = float(self.lineEdit_rate_of_feed.text())
            self.FINAL_2 = self.Working_Area * self.rate_of_feed / self.FINAL_1
            self.tabWidget.setCurrentIndex(3)
            for i in self.li:
                i.setPlainText(f'''Density = {self.density} gm/cm³
Atomic Weight = {self.atomic_weight} g/mole
Valency = {self.valency}
MRR = {float(round(self.FINAL_1, 3))} mm³/A.min
************************
Working Area = {self.Working_Area} mm²
Rate Of Feed = {self.rate_of_feed} mm/min
Current = {float(round(self.FINAL_2, 3))} Ampere
************************''')
            return self.FINAL_2, self.Working_Area
        except ValueError as e:
            print(e)
            QMessageBox.information(self, "Error", f"{e}")
    def mathematical3(self):
        try:
            self.voltage = float(self.lineEdit_voltage.text())
            self.FINAL_3 = self.voltage / self.FINAL_2
            self.tabWidget.setCurrentIndex(4)
            for i in self.li:
                i.setPlainText(f'''Density = {self.density} gm/cm³
Atomic Weight = {self.atomic_weight} g/mole 
Valency = {self.valency}
MRR = {float(round(self.FINAL_1, 3))} mm³/A.min
************************
Working Area = {self.Working_Area}
Rate Of Feed = {self.rate_of_feed}
Current = {float(round(self.FINAL_2, 3))} Ampere
************************
Voltage = {self.voltage} volt
Resistance = {float(round(self.FINAL_3, 3))} Ω''')
            return self.FINAL_3
        except ValueError as e:
            print(e)
            QMessageBox.information(self, "Error", f"{e}")
    def mathematical4(self):
        try:
            self.resistivity = float(self.lineEdit_Resistivity.text())
            self.Finally = self.FINAL_3 * self.Working_Area / self.resistivity
            for i in self.li:
                i.setPlainText(f'''Density = {self.density} gm/cm³
Atomic Weight = {self.atomic_weight} g/mole 
Valency = {self.valency}
MRR = {float(round(self.FINAL_1, 3))} mm³/A.min
************************
Working Area = {self.Working_Area}
Rate Of Feed = {self.rate_of_feed}
Current = {float(round(self.FINAL_2, 3))} Ampere
************************
Voltage = {self.voltage} volt
Resistance = {float(round(self.FINAL_3, 3))} Ω
************************
Resistivity = {self.resistivity}  (Ω.mm)
Machining gap = {float(round(self.Finally,3))} mm''')
            return self.Finally
        except ValueError as e:
            print(e)
            QMessageBox.information(self, "Error", f"{e}")
    def tap0(self): # FOR TAP 1
        self.tabWidget.setCurrentIndex(0)
    def tap1(self): # FOR TAP 2
        self.tabWidget.setCurrentIndex(1)
    def tap2(self): # FOR TAP 3
        self.tabWidget.setCurrentIndex(2)
    def tap3(self): # FOR TAP 4
        self.tabWidget.setCurrentIndex(3)
    def tap4(self):
        self.tabWidget.setCurrentIndex(4)

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
