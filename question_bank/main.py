import sys
from PyQt5.QtWidgets import QApplication
from login_function import Login


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginWindow = Login()
    loginWindow.show()
    sys.exit(app.exec_())
