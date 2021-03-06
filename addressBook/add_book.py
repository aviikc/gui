from PyQt5.QtWidgets import (
                            QWidget,QDialog, 
                            QMainWindow, QApplication, 
                            QMessageBox, QFileDialog,
                            QDialogButtonBox, QTableWidgetItem, 
                            QCheckBox, QButtonGroup, QComboBox
                        )
from PyQt5.QtGui import QFileOpenEvent, QPalette, QStandardItem
# from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt, QRunnable, QThreadPool, QObject
import sys, os


from Ui_main_diag import *
from Ui_add_new_dialg import *
import Ui_commerce
from database import init_db

from database import db_session
from contacts import Contact
from commerces import Commerce


# def check_dbfile():
#     os.chdir(os.path.dirname(__file__))
#     cwd = os.getcwd()
#     exists = os.path.isfile(cwd + '/tmp/test.db')
#     return exists    

# print(check_dbfile())


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton_addCon.clicked.connect(self.setup_contact)
        self.contact = Contact(self)
        self.contacts = self.contact.query.all()
        self.populateList(self.contacts)


    def populateList(self, contact_list):
        for i,row in enumerate(self.contacts):
            self.listWidget.addItem(row.first_name + " " + row.last_name + "Phone: " + row.mobile_number)


    def setup_contact(self):
        self.project = ContactWindow(parent=self)
        self.project.show()
        if self.project.exec_() == QDialog.Accepted:
            self.params = self.project.params
            self.loops = self.project.loops

    # def setup_commerce(self):
    #     self.project = CommerceWindow(parent=self)
    #     self.project.show()
    #     if self.project.exec_() == QDialog.Accepted:
    #         # print(self.project.params)
    #         # print("-----------------------")
    #         # print("-----------------------")
    #         # print(self.project.loops)
    #         self.params = self.project.params
    #         self.loops = self.project.loops



class ContactWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent=parent)
        self.setupUi(self)
        # self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.params = {}
        self.pushButton.pressed.connect(self.addContact)

    def addContact(self):        
        fName = self.lineEdit.text()
        lName = self.lineEdit_2.text()
        email = self.lineEdit_2.text()
        mobile = self.lineEdit_2.text()
        address = self.textEdit.toPlainText()
        # print(address)
        # print(type(address))
        # data_holder = Contact()
        cont = Contact(fName, lName, email, mobile, address)
        db_session.add(cont)
        db_session.commit()
        
        print("human contact added to db")
        self.close()

# class CommerceWindow(QtWidgets.QDialog, Ui_commerce.Ui_Dialog):
#     def __init__(self, parent=None):
#         QtWidgets.QDialog.__init__(self, parent=parent)
#         self.setupUi(self)
#         # self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
#         self.params = {}
#         self.pushButton.pressed.connect(self.clicked)

#     def clicked(self):
#         print("commercial contact added to db")
#         self.close()

if __name__ == '__main__':
    print("")
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    sys.exit(app.exec_())
    # print(check_dbfile())
    # if check_dbfile():
    #     from database import db_session
    #     print("yo")
    # else:
    #     os.mkdir(os.getcwd()+'tmp')
    #     from database import init_db
    # init_db()
    #     from database import db_session