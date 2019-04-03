# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Avik\Desktop\py\gui\gui\addressBook\main_diag.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(754, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_addCon = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addCon.setGeometry(QtCore.QRect(660, 40, 75, 23))
        self.pushButton_addCon.setObjectName("pushButton_addCon")
        self.listView_main = QtWidgets.QListView(self.centralwidget)
        self.listView_main.setGeometry(QtCore.QRect(30, 40, 621, 521))
        self.listView_main.setObjectName("listView_main")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(670, 530, 75, 23))
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_addComm = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addComm.setGeometry(QtCore.QRect(660, 80, 81, 23))
        self.pushButton_addComm.setObjectName("pushButton_addComm")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 754, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_addCon.setText(_translate("MainWindow", "Add Contact"))
        self.pushButton_close.setText(_translate("MainWindow", "Close"))
        self.pushButton_addComm.setText(_translate("MainWindow", "Add Commerce"))

