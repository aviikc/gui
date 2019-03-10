from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
import sys

class Frame(QWidget):
    def __init__(self):
        super(Frame, self).__init__()
        uic.loadUi("bmi_gui.ui", self)
        self.initUI()
    
    def initUI(self):
        self.pushButton_bmi.clicked.connect(self.onClick)
        self.pushButton_reset.clicked.connect(self.onReset)
        self.pushButton_close.clicked.connect(self.onClose)

    @pyqtSlot()
    def onClick(self):
        try:
            text_height = float(self.lineEdit_height.text())
            text_weight = float(self.lineEdit_weight.text())
            bmi = round(text_weight/(text_height/100)**2, 2)
            self.label_bmi.setText(str(bmi))
        except ValueError as e:
            self.label_bmi.setText(str(e))

    def onReset(self):
        self.lineEdit_height.setText(None)
        self.lineEdit_weight.setText(None)
        self.label_bmi.setText(None)

    def onClose(self):
        new_layout = QMessageBox.question(self, 'Quit Bmi Calculator?', 'Are you sure?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes )
        if new_layout == QMessageBox.Yes:
            sys.exit(0)
        else:
            print("Clicked No")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    frame = Frame()
    frame.show()
    sys.exit(app.exec_())