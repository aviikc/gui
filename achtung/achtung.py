from PyQt5.QtWidgets import QWidget,QApplication,QTimeEdit,QGridLayout
from PyQt5.QtCore import QTime

class Frame(QWidget):
    def __init__(self, parent = None):
        super(Frame, self).__init__(parent = parent)
        self.initUI()

    def initUI(self):
        myTime = QTime.currentTime()
        print(myTime)
        # self.layout = QGridLayout()
        # timewid = QTimeEdit(myTime)
        # self.layout.addWidget(timewid)


if __name__ == "__main__":
    app = QApplication([])
    frame = Frame()
    frame.show()
    app.exec_()