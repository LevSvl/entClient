# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.controls_label = QtWidgets.QLabel(MainWindow)
        self.controls_label.setGeometry(QtCore.QRect(30, 30, 81, 21))
        self.controls_label.setObjectName("controls_label")
        self.info_label = QtWidgets.QLabel(MainWindow)
        self.info_label.setGeometry(QtCore.QRect(30, 50, 300, 20))
        self.controls_label.setObjectName("keys_label")
        self.ingame_menu_close_button = QtWidgets.QPushButton(MainWindow)
        self.ingame_menu_close_button.setGeometry(QtCore.QRect(30, 250, 180, 40))
        self.ingame_menu_close_button.setObjectName("ingame_menu_close_button")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Settings"))
        self.controls_label.setText(_translate("MainWindow", "Управление:"))
        self.ingame_menu_close_button.setText(_translate("MainWindow", "Вернуться в главное меню"))
