import json
from PyQt5 import QtCore, QtGui, QtWidgets
from distribute_questions import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(582, 394)

        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(390, 290, 160, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(self.Continue)

        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.Exit)

        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 70, 160, 103))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(158, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)

        self.Marx = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.Marx.setFont(font)
        self.Marx.setObjectName("Marx")
        self.Marx.toggled.connect(self.subState)
        self.Marx.toggled.connect(lambda: self.btnstate(self.Marx))
        self.verticalLayout_2.addWidget(self.Marx)

        self.History = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.History.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.History.setFont(font)
        self.History.setObjectName("History")
        self.History.toggled.connect(self.subState)
        self.History.toggled.connect(lambda: self.btnstate(self.History))
        self.verticalLayout_2.addWidget(self.History)

        self.Moral = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Moral.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.Moral.setFont(font)
        self.Moral.setObjectName("Moral")
        self.Moral.toggled.connect(self.subState)
        self.Moral.toggled.connect(lambda: self.btnstate(self.Moral))
        self.verticalLayout_2.addWidget(self.Moral)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(250, 70, 101, 238))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setMaximumSize(QtCore.QSize(158, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)

        self.Chap00 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.Chap00.setFont(font)
        self.Chap00.setObjectName("Chap00")
        self.verticalLayout_3.addWidget(self.Chap00)
        self.Chap00.stateChanged.connect(lambda: self.btnstate(self.Chap00))
        self.Chap00.stateChanged.connect(lambda: self.chapState(self.Chap00))

        self.Chap01 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.Chap01.setFont(font)
        self.Chap01.setObjectName("Chap01")
        self.verticalLayout_3.addWidget(self.Chap01)
        self.Chap01.stateChanged.connect(lambda: self.btnstate(self.Chap01))
        self.Chap01.stateChanged.connect(lambda: self.chapState(self.Chap01))

        self.Chap02 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.Chap02.setFont(font)
        self.Chap02.setObjectName("Chap02")
        self.verticalLayout_3.addWidget(self.Chap02)
        self.Chap02.stateChanged.connect(lambda: self.btnstate(self.Chap02))
        self.Chap02.stateChanged.connect(lambda: self.chapState(self.Chap02))

        self.Chap03 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.Chap03.setFont(font)
        self.Chap03.setObjectName("Chap03")
        self.verticalLayout_3.addWidget(self.Chap03)
        self.Chap03.stateChanged.connect(lambda: self.btnstate(self.Chap03))
        self.Chap03.stateChanged.connect(lambda: self.chapState(self.Chap03))

        self.Chap04 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.Chap04.setFont(font)
        self.Chap04.setObjectName("Chap04")
        self.verticalLayout_3.addWidget(self.Chap04)
        self.Chap04.stateChanged.connect(lambda: self.btnstate(self.Chap04))
        self.Chap04.stateChanged.connect(lambda: self.chapState(self.Chap04))

        self.Chap05 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.Chap05.setFont(font)
        self.Chap05.setObjectName("Chap05")
        self.verticalLayout_3.addWidget(self.Chap05)
        self.Chap05.stateChanged.connect(lambda: self.btnstate(self.Chap05))
        self.Chap05.stateChanged.connect(lambda: self.chapState(self.Chap05))

        self.Chap06 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.Chap06.setFont(font)
        self.Chap06.setObjectName("Chap06")
        self.verticalLayout_3.addWidget(self.Chap06)
        self.Chap06.stateChanged.connect(lambda: self.btnstate(self.Chap06))
        self.Chap06.stateChanged.connect(lambda: self.chapState(self.Chap06))

        self.Chap07 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.Chap07.setFont(font)
        self.Chap07.setObjectName("Chap07")
        self.verticalLayout_3.addWidget(self.Chap07)
        self.Chap07.stateChanged.connect(lambda: self.btnstate(self.Chap07))
        self.Chap07.stateChanged.connect(lambda: self.chapState(self.Chap07))

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(400, 70, 139, 131))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setMinimumSize(QtCore.QSize(0, 20))
        self.label_3.setMaximumSize(QtCore.QSize(158, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)

        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(-1, 0, -1, 0)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")

        '''self.Type_Judge = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.Type_Judge.setFont(font)
        self.Type_Judge.setEnabled(False)
        self.Type_Judge.setCheckable(True)
        self.Type_Judge.setChecked(True)
        self.Type_Judge.setObjectName("Type_Judge")
        #self.verticalLayout_4.addWidget(self.Type_Judge)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Type_Judge)
        self.Type_Judge.stateChanged.connect(lambda: self.btnstate(self.Type_Judge))
        self.Type_Judge.stateChanged.connect(lambda: self.typeState(self.Type_Judge))

        self.Type_Sgl = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.Type_Sgl.setFont(font)
        self.Type_Sgl.setObjectName("Type_Sgl")
        self.Type_Sgl.setEnabled(False)
        self.Type_Sgl.setCheckable(True)
        self.Type_Sgl.setChecked(True)
        #self.verticalLayout_4.addWidget(self.Type_Sgl)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Type_Sgl)
        self.Type_Sgl.stateChanged.connect(lambda: self.btnstate(self.Type_Sgl))
        self.Type_Sgl.stateChanged.connect(lambda: self.typeState(self.Type_Sgl))

        self.Type_Mul = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.Type_Mul.setFont(font)
        self.Type_Mul.setObjectName("Type_Mul")
        self.Type_Mul.setEnabled(False)
        self.Type_Mul.setCheckable(True)
        self.Type_Mul.setChecked(True)
        #self.verticalLayout_4.addWidget(self.Type_Mul)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Type_Mul)
        self.Type_Mul.stateChanged.connect(lambda: self.btnstate(self.Type_Mul))
        self.Type_Mul.stateChanged.connect(lambda: self.typeState(self.Type_Mul))'''

        self.comboBox_Judge = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_Judge.setObjectName("comboBox_Judge")
        self.comboBox_Judge.currentIndexChanged.connect(self.selectionChange)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_Judge)

        self.comboBox_Sgl = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_Sgl.setObjectName("comboBox_Sgl")
        self.comboBox_Sgl.currentIndexChanged.connect(self.selectionChange)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox_Sgl)

        self.comboBox_Mul = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_Mul.setObjectName("comboBox_Mul")
        self.comboBox_Mul.currentIndexChanged.connect(self.selectionChange)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBox_Mul)

        self.verticalLayout_4.addLayout(self.formLayout)

        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        for n in range(1, 101):
            self.comboBox_Judge.addItem("{}".format(n))
            self.comboBox_Sgl.addItem("{}".format(n))
            self.comboBox_Mul.addItem("{}".format(n))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "进入顺序练习"))
        self.pushButton.setText(_translate("Dialog", "确认"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))
        self.label_4.setText(_translate("Dialog", "科目选择"))
        self.Marx.setText(_translate("Dialog", "马克思主义基本原理概论"))
        self.History.setText(_translate("Dialog", "中国近现代史纲要"))
        self.Moral.setText(_translate("Dialog", "思想道德修养与法律基础"))
        self.label_2.setText(_translate("Dialog", "章节选择"))
        self.Chap00.setText(_translate("Dialog", "绪论"))
        self.Chap01.setText(_translate("Dialog", "第一章"))
        self.Chap02.setText(_translate("Dialog", "第二章"))
        self.Chap03.setText(_translate("Dialog", "第三章"))
        self.Chap04.setText(_translate("Dialog", "第四章"))
        self.Chap05.setText(_translate("Dialog", "第五章"))
        self.Chap06.setText(_translate("Dialog", "第六章"))
        self.Chap07.setText(_translate("Dialog", "第七章"))
        self.label_3.setText(_translate("Dialog", "题型选择"))
        self.label_5.setText(_translate("Dialog", "判断题"))
        self.label_6.setText(_translate("Dialog", "单选题"))
        self.label_7.setText(_translate("Dialog", "多选题"))
        self.label.setText(_translate("Dialog", "专项选择"))

    def selectionChange(self):
        global d_Judge_num, d_Sgl_num, d_Mul_num
        d_Judge_num = self.comboBox_Judge.currentIndex()
        d_Sgl_num = self.comboBox_Sgl.currentIndex()
        d_Mul_num = self.comboBox_Mul.currentIndex()

    def Continue(self):
        d_type = "012"
        with open('exam_number.json', 'w', encoding='utf-8') as f1:
            dic = {"Judge": d_Judge_num + 1, "Single": d_Sgl_num + 1, "Multiple": d_Mul_num + 1}
            json.dump(dic, f1, ensure_ascii=False, indent=4)
        with open('exam_bank.json', 'w', encoding='utf-8') as f2:
            seq = []
            dic1 = {}
            dic2 = {}
            for question in distribute_question(d_sub, d_chap, d_type):
                seq.append(question[-1])
                dic1.update(dic2.fromkeys(seq, question[0:-1]))
                seq = []
                dic2 = {}
            json.dump(dic1, f2, ensure_ascii=False, indent=4)

    def Exit(self):
        exit()

    def subState(self):
        global d_sub

        if self.Marx.isChecked() == True:
            d_sub = 0
        if self.History.isChecked() == True:
            d_sub = 1
        if self.Moral.isChecked() == True:
            d_sub = 2

        d_sub = str(d_sub)

    def chapState(self, btn):
        global d_chap
        d_chap = set()
        str_name = "self.Chap0{0}.isChecked()"

        for i in range(0, 8):
            if eval(str_name.format(i)) == 1:
                d_chap.add(str(i))
            else:
                d_chap.discard(str(i))
        d_chap = ''.join(list(d_chap))


    '''def typeState(self, btn):
        global d_type
        d_type = set()

        if self.Type_Judge.isChecked() == True:
            d_type.add("0")
        else:
            d_type.discard("0")
        if self.Type_Sgl.isChecked() == True:
            d_type.add("1")
        else:
            d_type.discard("1")
        if self.Type_Mul.isChecked() == True:
            d_type.add("2")
        else:
            d_type.discard("2")

        d_type = ''.join(list(d_type))'''

    def btnstate(self, btn):
        judge1 = self.Marx.isChecked() or self.History.isChecked() or self.Moral.isChecked()
        judge2 = False
        str_name = "self.Chap0{0}.isChecked()"

        for i in range(0, 8):
            if eval(str_name.format(i)) == 1:
                judge2 = True
        if judge1:
            if judge2:
                self.pushButton.setEnabled(True)
            else:
                self.pushButton.setEnabled(False)

'''
    def btnstate(self, btn):
        if (self.Marx.isChecked() == True) or (self.History.isChecked() == True) or (self.Moral.isChecked() == True):
            if (self.Chap00.isChecked() == 0) or (self.Chap01.isChecked() == 0) or (self.Chap02.isChecked() == 0) or (self.Chap03.isChecked() == 0) or (self.Chap04.isChecked() == 0) or (self.Chap05.isChecked() == 0) or (self.Chap06.isChecked() == 0) or (self.Chap07.isChecked() == 0):
                if (self.Type_Judge.isChecked() == 0) or (self.Type_Sgl.isChecked() == 0) or (self.Type_Mul.isChecked() == 0):
                    self.pushButton.setEnabled(True)
'''

