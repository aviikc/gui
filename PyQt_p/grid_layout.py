import sys

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel

class Frame(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        self.setLayout(layout)
        label = QLabel("Hello Dude", self)
        layout.addWidget(label, 0, 0)

 
        label2 = QLabel("oK", self)
        layout.addWidget(label2, 0, 1)



if __name__ == "__main__":
     app = QApplication(sys.argv)
     frame = Frame()
     frame.show()
     app.exec_()