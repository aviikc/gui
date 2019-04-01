from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

from MainWindow import Ui_MainWindow
# Calculator state.
READY = 0
INPUT = 1

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle("Calculator")
        for n in range(0, 10):
            getattr(self, 'pushButton_%s' % n).pressed.connect(lambda v=n: self.input_number(v))
            self.pushButton_clear.pressed.connect(self.reset)

        self.reset()

        self.show()

    def display(self):
        self.lcdNumber.display(self.stack[-1])
        print(self.stack)
        # self.statusbar.showMessage(str("--".join(self.stack)))

    def reset(self):
        self.state = READY
        self.stack = [0]
        self.display()


    def input_number(self, v):
        if self.state == READY:
            self.state = INPUT
            self.stack[-1] = v
        else:
            self.stack[-1] = self.stack[-1] * 10 + v

        self.display()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()