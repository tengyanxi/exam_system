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
        self.button_exam = QtWidgets.QPushButton(self.centralwidget)
        self.button_exam.setGeometry(QtCore.QRect(200, 80, 400, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.button_exam.setFont(font)
        self.button_exam.setObjectName("button_exam")
        self.button_exercise = QtWidgets.QPushButton(self.centralwidget)
        self.button_exercise.setGeometry(QtCore.QRect(200, 210, 400, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.button_exercise.setFont(font)
        self.button_exercise.setObjectName("button_exercise")
        self.button_wrong = QtWidgets.QPushButton(self.centralwidget)
        self.button_wrong.setGeometry(QtCore.QRect(200, 340, 400, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.button_wrong.setFont(font)
        self.button_wrong.setObjectName("button_wrong")
        self.button_star = QtWidgets.QPushButton(self.centralwidget)
        self.button_star.setGeometry(QtCore.QRect(200, 470, 400, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.button_star.setFont(font)
        self.button_star.setObjectName("button_star")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(660, 30, 130, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(660, 60, 130, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(660, 90, 130, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "鸿蒙考试系统"))
        self.button_exam.setText(_translate("MainWindow", "模拟考试"))
        self.button_exercise.setText(_translate("MainWindow", "专项练习"))
        self.button_wrong.setText(_translate("MainWindow", "错题集"))
        self.button_star.setText(_translate("MainWindow", "收藏集"))
        self.radioButton.setText(_translate("MainWindow", "马克思主义原理"))
        self.radioButton_2.setText(_translate("MainWindow", "中国近代史史纲"))
        self.radioButton_3.setText(_translate("MainWindow", "思想道德修养"))
