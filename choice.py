# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choice.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_choiceWindow(object):
    def setupUi(self, choiceWindow):
        choiceWindow.setObjectName("choiceWindow")
        choiceWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(choiceWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.combo_single = QtWidgets.QComboBox(self.centralwidget)
        self.combo_single.setGeometry(QtCore.QRect(390, 105, 100, 40))
        self.combo_single.setObjectName("combo_single")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 255, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 405, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.combo_several = QtWidgets.QComboBox(self.centralwidget)
        self.combo_several.setGeometry(QtCore.QRect(390, 255, 100, 40))
        self.combo_several.setObjectName("combo_several")
        self.combo_decide = QtWidgets.QComboBox(self.centralwidget)
        self.combo_decide.setGeometry(QtCore.QRect(390, 405, 100, 40))
        self.combo_decide.setObjectName("combo_decide")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 20, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 510, 136, 46))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(260, 105, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        choiceWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(choiceWindow)
        QtCore.QMetaObject.connectSlotsByName(choiceWindow)

    def retranslateUi(self, choiceWindow):
        _translate = QtCore.QCoreApplication.translate
        choiceWindow.setWindowTitle(_translate("choiceWindow", "MainWindow"))
        self.lineEdit_2.setText(_translate("choiceWindow", "多选题"))
        self.lineEdit_3.setText(_translate("choiceWindow", "判断题"))
        self.lineEdit_4.setText(_translate("choiceWindow", "题型选择"))
        self.pushButton.setText(_translate("choiceWindow", "确认"))
        self.lineEdit.setText(_translate("choiceWindow", "单选题"))
