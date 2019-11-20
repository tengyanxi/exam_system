from registerWindow import Ui_registerWindow
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QMessageBox

name_pwd = {"PeiLei":"123456", "DingYuLong":"123456"}

class register(Ui_registerWindow,QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        '''self._name = self.lineEdit_register_name.text()
        self._pwd1 = self.lineEdit_register_pwd1.text()
        self._pwd2 = self.lineEdit_register_pwd2.text()'''
        self.confirmButton.clicked.connect(self.confirmButton_click)
        self.returnButton.clicked.connect(self.returnButton_click)
        self.lineEdit_register_name.textChanged.connect(self.showTip2)
        self.lineEdit_register_pwd2.textChanged.connect(self.showTip3)
        regx = QRegExp("^[a-zA-Z][0-9A-Za-z]{14}$")  # 为给定的模式字符串构造一个正则表达式对象。

        #此处规定密码不超过14位，后续需修改：密码控制在6 - 14 位；用户名只能有字母、数字和下划线，并且以字母开头

        validator = QRegExpValidator(regx,self.lineEdit_register_pwd1)  # 构造一个验证器，该父对象接受与正则表达式匹配的所有字符串。这里的父对象就是QLineEdit对象了。匹配是针对整个字符串; 例如：如果正则表达式是[A-Fa-f0-9]+将被视为^[A-Fa-f0-9]+$。
        self.lineEdit_register_pwd1.setValidator(validator) #字母开头，只能有数字和字母，不超过14位

    def showTip2(self):   #注册界面用户名已被注册提示
        if self.lineEdit_register_name.text() in name_pwd:
            self.tip_label2.setText("该用户名已被注册！")
        else:
            self.tip_label2.setText("")

    def showTip3(self):   #注册界面密码输入不一致提示，后续需修改：当tip_label3失去焦点时才进行判断两次输入的密码是否一致
        self._pwd1 = self.lineEdit_register_pwd1.text()
        self._pwd2 = self.lineEdit_register_pwd2.text()
        if self._pwd1 != self._pwd2: #and self.lineEdit_register_pwd2.FocusOut():
            self.tip_label3.setText("两次输入的密码不一致！")
        else:
            self.tip_label3.setText("")
    def confirmButton_click(self):
        if self.lineEdit_register_name.text() not in name_pwd and self.lineEdit_register_pwd1.text() == self.lineEdit_register_pwd2.text():
            name_pwd[self.lineEdit_register_name.text()] = self.lineEdit_register_pwd1.text()
            QMessageBox.information(self, "注册成功", "注册成功！", QMessageBox.Yes)
            self.close()
            #loginWindow.show()
        else:
            QMessageBox.warning(self, "注册失败", "注册失败，请重新输入！", QMessageBox.Yes)
            #可以清空也可以不清空

    def returnButton_click(self):
        self.close()

    def closeEvent(self, event):   #窗体关闭时执行清空
        self.lineEdit_register_name.setText("")
        self.lineEdit_register_pwd1.setText("")
        self.lineEdit_register_pwd2.setText("")
        self.lineEdit_register_name.setFocus()