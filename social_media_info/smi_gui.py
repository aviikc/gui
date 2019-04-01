from PyQt5.QtWidgets import (QWidget, QMainWindow,
                            QApplication)
from PyQt5 import uic
import sys


class Frame(QMainWindow):
    
    def __init__(self,  parent = None):
        super(Frame, self).__init__(parent = parent)        
        uic.loadUi(r"ui_files\\main_smi_window.ui", self)
        self.initUI()
        self.buttonEvents()

    def initUI(self):
        '''
            Initial Gui
        ''' 
        pass

    def buttonEvents(self):
        '''
            Method to channel signals to slots
        '''        
        self.pushButton_close.clicked.connect(self.onCloseEvent)  #close button


    def onCloseEvent(self):
        '''
            When Close Button is Pressed
        ''' 
        sys.exit(0)




if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    frame = Frame()
    frame.show()
    sys.exit(app.exec_())

