import sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QMainWindow, QMessageBox
from loginWindow import Ui_loginWindow
from registerWindow import Ui_registerWindow
from functools import partial

name_pwd = {"PeiLei":"123456", "DingYuLong":"123456"}

class Example(Ui_loginWindow,QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self._name = ""
        self._pwd = ""
        self.loginButton.clicked.connect(self.loginButton_click)
        self.registerButton.clicked.connect(self.registerButton_click)
        self.lineEdit_name.textChanged.connect(self.showTip)

    def showTip(self):    #用户名不存在提示
        if self.lineEdit_name.text() not in name_pwd:
            self.tip_label.setText("用户名不存在！")
        else:
            self.tip_label.setText("")

    def loginButton_click(self):
        self._name = self.lineEdit_name.text()
        self._pwd = self.lineEdit_pwd.text()
        if self._name in name_pwd and self._pwd == name_pwd[self._name]:
            reply = QMessageBox.information(self, "登录成功", "登录成功", QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                #newWindow.show()
                self.close()
        else:
            QMessageBox.warning(self, "登陆失败", "用户名或密码错误", QMessageBox.Yes)
            self.lineEdit_pwd.setText("")
            self.lineEdit_pwd.setFocus()

    def registerButton_click(self):
        registerWindow.show()
        self.lineEdit_name.setText("")
        self.lineEdit_pwd.setText("")
        self.tip_label.setText("")

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
        validator = QRegExpValidator(regx,self.lineEdit_register_pwd1)  # 构造一个验证器，该父对象接受与正则表达式匹配的所有字符串。这里的父对象就是QLineEdit对象了。匹配是针对整个字符串; 例如：如果正则表达式是[A-Fa-f0-9]+将被视为^[A-Fa-f0-9]+$。
        self.lineEdit_register_pwd1.setValidator(validator) #字母开头，只能有数字和字母，不超过14位

    def showTip3(self):
        self._pwd1 = self.lineEdit_register_pwd1.text()
        self._pwd2 = self.lineEdit_register_pwd2.text()
        if self._pwd1 != self._pwd2: #and self.lineEdit_register_pwd2.FocusOut():
            self.tip_label3.setText("两次输入的密码不一致！")
        else:
            self.tip_label3.setText("")

    def showTip2(self):
        if self.lineEdit_register_name.text() in name_pwd:
            self.tip_label2.setText("该用户名已被注册！")
        else:
            self.tip_label2.setText("")

    def confirmButton_click(self):
        if self.lineEdit_register_name.text() not in name_pwd and self.lineEdit_register_pwd1.text() == self.lineEdit_register_pwd2.text():
            name_pwd[self.lineEdit_register_name.text()] = self.lineEdit_register_pwd1.text()
            QMessageBox.information(self, "注册成功", "注册成功！", QMessageBox.Yes)
            self.close()
            loginWindow.show()
        else:
            QMessageBox.warning(self, "注册失败", "注册失败，请重新输入！", QMessageBox.Yes)
            #可以清空也可以不清空

    def returnButton_click(self):
        self.close()

    def closeEvent(self, event): #窗体关闭时执行清空
        self.lineEdit_register_name.setText("")
        self.lineEdit_register_pwd1.setText("")
        self.lineEdit_register_pwd2.setText("")
        self.lineEdit_register_name.setFocus()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginWindow = Example()
    loginWindow.show()
    registerWindow = register()
    sys.exit(app.exec_())