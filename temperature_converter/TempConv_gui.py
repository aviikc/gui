from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
import sys
from configparser import ConfigParser

covert_options = ["Celcius to Farenheit", "Celcius to Kelvin", "Farenheit to Celcius", "Farenheit to Kelvin", "Kelvin to Celcius", "Kelvin to Farenheit"]
class Frame(QWidget):
    def __init__(self):
        super(Frame, self).__init__()
        uic.loadUi("temperature_converter.ui", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Temperature Converter")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    frame = Frame()
    frame.show()
    sys.exit(app.exec_())