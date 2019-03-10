from PyQt5.QtWidgets import QWidget, QApplication, QComboBox, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
import sys


convert_options = ["Celcius to Farenheit", "Celcius to Kelvin", "Farenheit to Celcius", "Farenheit to Kelvin", "Kelvin to Celcius", "Kelvin to Farenheit"]
class Frame(QWidget):
    def __init__(self):
        super(Frame, self).__init__()
        uic.loadUi("com_check.ui", self)
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle("Temperature Converter")
        self.comboBox_choices.addItems(convert_options)
        self.comboBox_choices.currentTextChanged.connect(self.onClick)

    @pyqtSlot()
    def onClick(self):
        self.label_output.setText(self.comboBox_choices.currentText())
        
        

    
        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    frame = Frame()
    frame.show()
    sys.exit(app.exec_())