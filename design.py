# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1018, 353)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.find_workers_btn = QtWidgets.QPushButton(self.centralwidget)
        self.find_workers_btn.setGeometry(QtCore.QRect(40, 250, 171, 28))
        self.find_workers_btn.setObjectName("find_workers_btn")
        self.work_label = QtWidgets.QLabel(self.centralwidget)
        self.work_label.setGeometry(QtCore.QRect(0, 0, 269, 16))
        self.work_label.setObjectName("work_label")
        self.work_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.work_edit.setGeometry(QtCore.QRect(0, 20, 291, 24))
        self.work_edit.setObjectName("work_edit")
        self.payment_label = QtWidgets.QLabel(self.centralwidget)
        self.payment_label.setGeometry(QtCore.QRect(0, 50, 269, 16))
        self.payment_label.setObjectName("payment_label")
        self.payment_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.payment_edit.setGeometry(QtCore.QRect(0, 70, 291, 24))
        self.payment_edit.setObjectName("payment_edit")
        self.city_label = QtWidgets.QLabel(self.centralwidget)
        self.city_label.setGeometry(QtCore.QRect(0, 100, 269, 16))
        self.city_label.setObjectName("city_label")
        self.city_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.city_edit.setGeometry(QtCore.QRect(0, 120, 291, 24))
        self.city_edit.setObjectName("city_edit")
        self.age_label = QtWidgets.QLabel(self.centralwidget)
        self.age_label.setGeometry(QtCore.QRect(0, 150, 269, 16))
        self.age_label.setObjectName("age_label")
        self.age_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.age_edit.setGeometry(QtCore.QRect(0, 170, 291, 24))
        self.age_edit.setObjectName("age_edit")
        self.sex_label = QtWidgets.QLabel(self.centralwidget)
        self.sex_label.setGeometry(QtCore.QRect(0, 200, 269, 16))
        self.sex_label.setObjectName("sex_label")
        self.sex_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.sex_edit.setGeometry(QtCore.QRect(0, 220, 291, 24))
        self.sex_edit.setObjectName("sex_edit")
        self.error_label = QtWidgets.QLabel(self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(10, 650, 321, 41))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 20, 121, 21))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 20, 121, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(570, 20, 121, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(700, 20, 121, 21))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(820, 20, 141, 21))
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(310, 50, 651, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.json_btn = QtWidgets.QPushButton(self.centralwidget)
        self.json_btn.setGeometry(QtCore.QRect(482, 250, 201, 28))
        self.json_btn.setObjectName("json_btn")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(310, 150, 51, 41))
        self.label_11.setObjectName("label_11")
        self.url_label = QtWidgets.QLabel(self.centralwidget)
        self.url_label.setGeometry(QtCore.QRect(360, 160, 421, 21))
        self.url_label.setText("")
        self.url_label.setObjectName("url_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1018, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Внезапный квинтет"))
        self.find_workers_btn.setText(_translate("MainWindow", "Найти работников"))
        self.work_label.setText(_translate("MainWindow", "Должность"))
        self.payment_label.setText(_translate("MainWindow", "Зарплата"))
        self.city_label.setText(_translate("MainWindow", "Город / Регион"))
        self.age_label.setText(_translate("MainWindow", "Возраст"))
        self.sex_label.setText(_translate("MainWindow", "Пол"))
        self.label.setText(_translate("MainWindow", "Должность"))
        self.label_3.setText(_translate("MainWindow", "Зарплата"))
        self.label_4.setText(_translate("MainWindow", "Город"))
        self.label_5.setText(_translate("MainWindow", "Возраст"))
        self.label_2.setText(_translate("MainWindow", "Пол"))
        self.json_btn.setText(_translate("MainWindow", "Сохранить результат в json"))
        self.label_11.setText(_translate("MainWindow", "Ссылка:"))