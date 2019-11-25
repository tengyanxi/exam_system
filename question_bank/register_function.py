from register_window import Ui_register_window
from data_operation import judge_in, write_data
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QMessageBox


class Register(Ui_register_window, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()
        self._pwd1 = ""
        self._pwd2 = ""
        self._name = ""

    def initUi(self):
        self.confirmButton.clicked.connect(self.confirm_button_click)
        self.returnButton.clicked.connect(self.return_button_click)
        self.lineEditRegisterName.textChanged.connect(self.show_tip2)
        self.lineEditRegisterPwd2.textChanged.connect(self.show_tip3)
        regx = QRegExp("^[a-zA-Z][0-9A-Za-z]{14}$")   # 为给定的模式字符串构造一个正则表达式对象。

        # 此处规定密码不超过14位，后续需修改：密码控制在6 - 14 位；用户名只能有字母、数字和下划线，并且以字母开头

        validator = QRegExpValidator(regx, self.lineEditRegisterPwd1)
        # 构造一个验证器，该父对象接受与正则表达式匹配的所有字符串。这里的父对象就是QLineEdit对象了。
        # 匹配是针对整个字符串; 例如：如果正则表达式是[A-Fa-f0-9]+将被视为^[A-Fa-f0-9]+$。

        self.lineEditRegisterPwd1.setValidator(validator)   # 字母开头，只能有数字和字母，不超过14位

    def show_tip2(self):   # 注册界面用户名已被注册提示
        if judge_in(self.lineEditRegisterName.text()):
            self.tipLabel2.setText("该用户名已被注册！")
        else:
            self.tipLabel2.setText("")

    def show_tip3(self):   # 注册界面密码输入不一致提示，后续需修改：当tip_label3失去焦点时才进行判断两次输入的密码是否一致
        self._pwd1 = self.lineEditRegisterPwd1.text()
        self._pwd2 = self.lineEditRegisterPwd2.text()
        if self._pwd1 != self._pwd2:   # and self.lineEdit_register_pwd2.FocusOut(): 没有FocusOut()这个方法
            self.tipLabel3.setText("两次输入的密码不一致！")
        else:
            self.tipLabel3.setText("")

    def confirm_button_click(self):
        self._name = self.lineEditRegisterName.text()
        self._pwd1 = self.lineEditRegisterPwd1.text()
        self._pwd2 = self.lineEditRegisterPwd2.text()
        if not judge_in(self._name) and self._pwd1 == self.pwd2:
            write_data(self._name, self._pwd1)
            QMessageBox.information(self, "注册成功", "注册成功！", QMessageBox.Yes)
            self.close()
            # loginWindow.show()
        else:
            QMessageBox.warning(self, "注册失败", "注册失败，请重新输入！", QMessageBox.Yes)
            # 可以清空也可以不清空

    def return_button_click(self):
        self.close()

    def closeEvent(self, event):   # 窗体关闭时执行清空
        self.lineEditRegisterName.setText("")
        self.lineEditRegisterPwd1.setText("")
        self.lineEditRegisterPwd2.setText("")
        self.lineEditRegisterName.setFocus()
