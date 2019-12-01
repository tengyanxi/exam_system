# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_addfile = QtWidgets.QPushButton(self.centralwidget)
        self.button_addfile.setGeometry(QtCore.QRect(630, 15, 150, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_addfile.setFont(font)
        self.button_addfile.setObjectName("button_addfile")
        self.button_exam = QtWidgets.QPushButton(self.centralwidget)
        self.button_exam.setGeometry(QtCore.QRect(200, 90, 400, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.button_exam.setFont(font)
        self.button_exam.setObjectName("button_exam")
        self.button_exercise = QtWidgets.QPushButton(self.centralwidget)
        self.button_exercise.setGeometry(QtCore.QRect(200, 290, 400, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.button_exercise.setFont(font)
        self.button_exercise.setObjectName("button_exercise")
        self.button_wrong = QtWidgets.QPushButton(self.centralwidget)
        self.button_wrong.setGeometry(QtCore.QRect(200, 490, 400, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.button_wrong.setFont(font)
        self.button_wrong.setObjectName("button_wrong")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_addfile.setText(_translate("MainWindow", "添加题库文件"))
        self.button_exam.setText(_translate("MainWindow", "模拟考试"))
        self.button_exercise.setText(_translate("MainWindow", "专项练习"))
        self.button_wrong.setText(_translate("MainWindow", "错题集"))
