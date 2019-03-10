from PyQt5.QtWidgets import QWidget, QApplication, QComboBox, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
import sys
from configparser import ConfigParser
import Temp_convert


convert_options = ["Celcius to Farenheit", "Celcius to Kelvin", "Farenheit to Celcius", "Farenheit to Kelvin", "Kelvin to Celcius", "Kelvin to Farenheit"]
class Frame(QWidget):
    def __init__(self):
        super(Frame, self).__init__()
        uic.loadUi("temperature_converter.ui", self)
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle("Temperature Converter")
        self.comboBox_choices.addItems(convert_options)
        self.button_choices()
        self.label_unit.setText(chr(176) + "C")

    def button_choices(self):
        self.comboBox_choices.currentTextChanged.connect(self.onChange)
        self.pushButton_convert.clicked.connect(self.onClick)
        self.pushButton_reset.clicked.connect(self.onReset)
        self.pushButton_cancel.clicked.connect(self.onClose)

    @pyqtSlot()
    def onClick(self):
        try:
            input_temp_value = float(self.lineEdit_temp.text())
            comboText = self.comboBox_choices.currentText()
            if comboText == "Celcius to Farenheit":
                converted_temp = self.cel_to_far(input_temp_value)
                self.label_output.setText(str(converted_temp) + chr(176) + "F")
            elif comboText == "Celcius to Kelvin":
                converted_temp = self.cel_to_kel(input_temp_value)
                self.label_output.setText(str(converted_temp) + chr(176) + "K")
            elif comboText == "Farenheit to Celcius":
                converted_temp = self.far_to_cel(input_temp_value)
                self.label_output.setText(str(converted_temp) + chr(176) + "C")
            elif comboText == "Farenheit to Kelvin":
                converted_temp = self.far_to_kel(input_temp_value)
                self.label_output.setText(str(converted_temp) + chr(176) + "K")
            elif comboText == "Kelvin to Celcius":
                converted_temp = self.kel_to_cel(input_temp_value)
                self.label_output.setText(str(converted_temp) + chr(176) + "C")
            elif comboText == "Kelvin to Farenheit":
                converted_temp = self.kel_to_far(input_temp_value)
                self.label_output.setText(str(converted_temp) + chr(176) + "F")
        except (ValueError, TypeError):
            self.label_output.setText("Invalid Input")

    def onChange(self):
        comboText = self.comboBox_choices.currentText()
        if comboText == "Celcius to Farenheit" or comboText == "Celcius to Kelvin":
            ext = (chr(176) + "C")
        elif comboText == "Farenheit to Celcius" or comboText == "Farenheit to Kelvin":
            ext = (chr(176) + "F")
        elif comboText == "Kelvin to Celcius" or comboText == "Kelvin to Farenheit":
            ext = (chr(176) + "K")
        self.label_unit.setText(ext)

    def cel_to_far(self, temp):
        return round(((temp*(9/5)) + 32), 2)

    def far_to_cel(self, temp):
        return round(((temp - 32)*(5/9)))

    def far_to_kel(self, temp):
        return round(((temp - 32)*(5/9) + 273.15), 2)

    def cel_to_kel(self, temp):
        return round((temp + 273.15), 2)

    def kel_to_cel(self, temp):
        return round((temp - 273.15), 2)

    def kel_to_far(self, temp):
        return round(((9/5)*(temp - 273.15) + 32), 2)

    def onReset(self):
        self.label_output.setText(None)
        self.label_unit.setText(chr(176) + "C")
        self.lineEdit_temp.setText(None)
        self.comboBox_choices.setCurrentIndex(0)

    def onClose(self):
        new_layout = QMessageBox.question(self, "Quit Converter", "Are You Sure", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if new_layout == QMessageBox.Yes:
            sys.exit(0)
        else:
            print(" ")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    frame = Frame()
    frame.show()
    sys.exit(app.exec_())