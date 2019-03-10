from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
import sys

class Frame(QWidget):
    def __init__(self):
        super(Frame, self).__init__()
        uic.loadUi("bmi_gui.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    frame = Frame()
    frame.show()
    sys.exit(app.exec_())
