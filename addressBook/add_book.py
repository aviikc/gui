from PyQt5.QtWidgets import QWidget,QDialog, QMainWindow, QApplication, QMessageBox, QFileDialog,QDialogButtonBox, QTableWidgetItem, QCheckBox, QButtonGroup, QComboBox
from PyQt5.QtGui import QFileOpenEvent, QPalette
# from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt, QRunnable, QThreadPool, QObject
import sys


from Ui_main_diag import *
from Ui_add_new_dialg import *
import Ui_commerce

from db_model import Contact


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton_addCon.clicked.connect(self.setup_contact)
        self.pushButton_addComm.clicked.connect(self.setup_commerce)

    def setup_contact(self):
        self.project = ContactWindow(parent=self)
        self.project.show()
        if self.project.exec_() == QDialog.Accepted:
            self.params = self.project.params
            self.loops = self.project.loops

    def setup_commerce(self):
        self.project = CommerceWindow(parent=self)
        self.project.show()
        if self.project.exec_() == QDialog.Accepted:
            self.params = self.project.params
            self.loops = self.project.loops



class ContactWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent=parent)
        self.setupUi(self)
        # self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.params = {}
        self.pushButton.pressed.connect(self.clicked)

    def clicked(self):
        fName = self.lineEdit.text()
        lName = self.lineEdit_2.text()
        email = self.lineEdit_2.text()
        mobile = self.lineEdit_2.text()
        address = self.textEdit.document()
        cont = Contact(fName,lName, email, mobile,address)
        print("human contact added to db")
        self.close()

class CommerceWindow(QtWidgets.QDialog, Ui_commerce.Ui_Dialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent=parent)
        self.setupUi(self)
        # self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.params = {}
        self.pushButton.pressed.connect(self.clicked)

    def clicked(self):
        print("commercial contact added to db")
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    sys.exit(app.exec_())
