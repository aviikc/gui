import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot




class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Folder Maker"
        self.left = 40
        self.top = 40
        self.height = 400
        self.width = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        # my_post = ""

        myLabel = QLabel(" my_post", self)
        myLabel.move(20, 100)

        button1 = QPushButton("Click", self)
        button1.move(50, 100)
        button1.clicked.connect(self.someSignal)




        self.show()



    @pyqtSlot()
    def someSignal(self):
        print("Hello World!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

