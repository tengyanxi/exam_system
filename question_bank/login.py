import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from loginWindow import Ui_loginWindow
from register import register
from DataOperation import judgeIn, judgeMatch

class login(Ui_loginWindow,QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        #self._name = ""
        #self._pwd = ""
        self.loginButton.clicked.connect(self.loginButton_click)
        self.registerButton.clicked.connect(self.registerButton_click)
        self.lineEdit_name.textChanged.connect(self.showTip)

    def showTip(self):    #登陆界面用户名不存在提示，后续需修改：tip_label失去焦点时才触发判断用户名存在的事件
        if not judgeIn(self.lineEdit_name.text()):
            self.tip_label.setText("用户名不存在！")
        else:
            self.tip_label.setText("")

    def loginButton_click(self):
        #self._name = self.lineEdit_name.text()
        #self._pwd = self.lineEdit_pwd.text()
        if judgeIn(self.lineEdit_name.text()) and judgeMatch(self.lineEdit_name.text(), self.lineEdit_pwd.text()):
            reply = QMessageBox.information(self, "登录成功", "登录成功", QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                #newWindow.show()  登陆成功后跳转新界面
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginWindow = login()
    loginWindow.show()
    registerWindow = register()
    sys.exit(app.exec_())