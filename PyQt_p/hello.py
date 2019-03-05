import sys

from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class Frame(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "My Folder Maker App"
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()

        textArea = QLineEdit(self)
        layout.addWidget(textArea)


        buttonA = QPushButton("OK", self)
        layout.addWidget(buttonA)







if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Frame()
    ex.show()
    sys.exit(app.exec_())
