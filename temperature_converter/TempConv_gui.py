from PyQt5.QtWidgets import QWidget, QApplication, QComboBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
import sys
from configparser import ConfigParser

convert_options = ["Celcius to Farenheit", "Celcius to Kelvin", "Farenheit to Celcius", "Farenheit to Kelvin", "Kelvin to Celcius", "Kelvin to Farenheit"]
class Frame(QWidget):
    def __init__(self):
        super(Frame, self).__init__()
        uic.loadUi("temperature_converter.ui", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Temperature Converter")
        self.comboBox.addItems(convert_options)
        comboText = self.comboBox.currentText()
 
        if comboText == "Celcius to Farenheit":
            self.label_2.setText(chr(176) + "C")
        elif comboText == "Celcius to Kelvin":
            self.label_2.setText(chr(176) + "C")
        elif comboText == "Farenheit to Celcius":
            self.label_2.setText(chr(176) + "F")
        elif comboText == "Farenheit to Kelvin":
            self.label_2.setText(chr(176) + "F")
        elif comboText == "Kelvin to Celcius":
            self.label_2.setText(chr(176) + "K")
        elif comboText == "Kelvin to Farenheit":
            self.label_2.setText(chr(176) + "K")
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    frame = Frame()
    frame.show()
    sys.exit(app.exec_())