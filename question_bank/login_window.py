# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login_window(object):
    def setupUi(self, login_window):
        login_window.setObjectName("login_window")
        login_window.resize(649, 428)
        self.centralwidget = QtWidgets.QWidget(login_window)
        self.centralwidget.setObjectName("centralwidget")
        self.labelName = QtWidgets.QLabel(self.centralwidget)
        self.labelName.setGeometry(QtCore.QRect(130, 110, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.labelName.setFont(font)
        self.labelName.setObjectName("labelName")
        self.labelPwd = QtWidgets.QLabel(self.centralwidget)
        self.labelPwd.setGeometry(QtCore.QRect(130, 190, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.labelPwd.setFont(font)
        self.labelPwd.setObjectName("labelPwd")
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
        self.lineEditName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditName.setGeometry(QtCore.QRect(230, 110, 261, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.lineEditName.setFont(font)
        self.lineEditName.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditPwd = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPwd.setGeometry(QtCore.QRect(230, 180, 261, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.lineEditPwd.setFont(font)
        self.lineEditPwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPwd.setObjectName("lineEditPwd")
        self.tipLabel = QtWidgets.QLabel(self.centralwidget)
        self.tipLabel.setGeometry(QtCore.QRect(500, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.tipLabel.setFont(font)
        self.tipLabel.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tipLabel.setToolTip("")
        self.tipLabel.setToolTipDuration(-1)
        self.tipLabel.setStyleSheet("color: rgb(255, 45, 8);")
        self.tipLabel.setText("")
        self.tipLabel.setObjectName("tipLabel")
        login_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(login_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 649, 26))
        self.menubar.setObjectName("menubar")
        login_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(login_window)
        self.statusbar.setObjectName("statusbar")
        login_window.setStatusBar(self.statusbar)

        self.retranslateUi(login_window)
        QtCore.QMetaObject.connectSlotsByName(login_window)

    def retranslateUi(self, login_window):
        _translate = QtCore.QCoreApplication.translate
        login_window.setWindowTitle(_translate("login_window", "登陆界面"))
        self.labelName.setText(_translate("login_window", "用户名："))
        self.labelPwd.setText(_translate("login_window", "密码："))
        self.loginButton.setText(_translate("login_window", "登录"))
        self.registerButton.setText(_translate("login_window", "注册"))
        self.lineEditName.setPlaceholderText(_translate("login_window", "请输入您的账号："))
        self.lineEditPwd.setPlaceholderText(_translate("login_window", "请输入您的密码："))
