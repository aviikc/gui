from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtCore import pyqtSlot
import sys

class Frame(QWidget):
    def __init__(self):        
        super().__init__()
        self.title = "Meter to Feet Converter"        
        self.initUI()


    def initUI(self):        
        layout = QGridLayout()
        self.label = QLabel("Meter to Feet Converter")
        self.input_value = QLineEdit()
        self.meter_label = QLabel("Metres")
        self.op_value_label = QLabel(" ")
        self.button01 = QPushButton("Calculate")
        self.button01.clicked.connect(self.onClick)

        layout.addWidget(self.label, 0, 1)
        layout.addWidget(self.input_value, 1, 1)
        layout.addWidget(self.meter_label, 1, 2)
        layout.addWidget(self.op_value_label, 2, 1)
        layout.addWidget(self.button01,3, 1)
        self.setLayout(layout)
        self.setWindowTitle(self.title)

    @pyqtSlot()
    def onClick(self):
        textBoxValue = int(self.input_value.text())
        foo = 3.28084 * textBoxValue
        self.op_value_label.setText(str(foo))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    frame = Frame()
    frame.show()    
    sys.exit(app.exec_())