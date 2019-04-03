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
        MainWindow.resize(436, 404)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(350, 330, 75, 23))
        self.pushButton_close.setObjectName("pushButton_close")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 331, 321))
        self.listWidget.setObjectName("listWidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(350, 40, 82, 83))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_addCon = QtWidgets.QPushButton(self.widget)
        self.pushButton_addCon.setObjectName("pushButton_addCon")
        self.verticalLayout.addWidget(self.pushButton_addCon)
        self.pushButton_addComm = QtWidgets.QPushButton(self.widget)
        self.pushButton_addComm.setObjectName("pushButton_addComm")
        self.verticalLayout.addWidget(self.pushButton_addComm)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 436, 21))
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
        self.pushButton_close.setText(_translate("MainWindow", "Close"))
        self.pushButton_addCon.setText(_translate("MainWindow", "Add Contact"))
        self.pushButton_addComm.setText(_translate("MainWindow", "Delete Contact"))
        self.pushButton.setText(_translate("MainWindow", "Edit Contact"))

