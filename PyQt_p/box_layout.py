from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
# Layout Style
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(layout)
        label = QLabel("label 1")
        layout.addWidget(label, 0)

        label2 = QLabel("Label2")
        layout.addWidget(label2, 1)

        # layout2 = QBoxLayout(QBoxLayout.TopToBottom)
        # self.setLayout(layout2)

        # label3 = QLabel("Label3")
        # layout2.addWidget(label3, 0)

        layout2 = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addLayout(layout2)
        label = QLabel("Label 3")
        layout2.addWidget(label, 0)
        label = QLabel("Label 4")
        layout2.addWidget(label, 0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
