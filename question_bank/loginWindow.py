# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(649, 428)
        self.centralwidget = QtWidgets.QWidget(loginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(130, 110, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.label_pwd = QtWidgets.QLabel(self.centralwidget)
        self.label_pwd.setGeometry(QtCore.QRect(130, 190, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_pwd.setFont(font)
        self.label_pwd.setObjectName("label_pwd")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(130, 260, 131, 51))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QtCore.QRect(360, 260, 131, 51))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.registerButton.setFont(font)
        self.registerButton.setObjectName("registerButton")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(230, 110, 261, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pwd.setGeometry(QtCore.QRect(230, 180, 261, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.lineEdit_pwd.setFont(font)
        self.lineEdit_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.tip_label = QtWidgets.QLabel(self.centralwidget)
        self.tip_label.setGeometry(QtCore.QRect(500, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.tip_label.setFont(font)
        self.tip_label.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tip_label.setToolTip("")
        self.tip_label.setToolTipDuration(-1)
        self.tip_label.setStyleSheet("color: rgb(255, 45, 8);")
        self.tip_label.setText("")
        self.tip_label.setObjectName("tip_label")
        loginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 649, 26))
        self.menubar.setObjectName("menubar")
        loginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loginWindow)
        self.statusbar.setObjectName("statusbar")
        loginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "登陆界面"))
        self.label_name.setText(_translate("loginWindow", "用户名："))
        self.label_pwd.setText(_translate("loginWindow", "密码："))
        self.loginButton.setText(_translate("loginWindow", "登录"))
        self.registerButton.setText(_translate("loginWindow", "注册"))
        self.lineEdit_name.setPlaceholderText(_translate("loginWindow", "请输入您的账号："))
        self.lineEdit_pwd.setPlaceholderText(_translate("loginWindow", "请输入您的密码："))
