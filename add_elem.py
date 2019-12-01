import sys
from choice import Ui_choiceWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication

class choice_window(Ui_choiceWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()
        for i in range(1,101):
            self.combo_decide.addItem(str(i))
            self.combo_several.addItem(str(i))
            self.combo_single.addItem(str(i))
        self.combo_decide.currentIndexChanged.connect(self.selectionchange_decide)
        self.combo_several.currentIndexChanged.connect(self.selectionchange_several)
        self.combo_single.currentIndexChanged.connect(self.selectionchange_single)


    def initUi(self):
        self.pushButton.clicked.connect(self.pushButton_click)
        self.pushButton.clicked.connect(QCoreApplication.instance().quit)

    def pushButton_click(self):
        pass

    def selectionchange_decide(self):
        decide_num = self.combo_decide.currentText()
        print(decide_num)

    def selectionchange_several(self):
        several_num = self.combo_several.currentText()
        print(several_num)

    def selectionchange_single(self):
        single_num = self.combo_single.currentText()
        print(single_num)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    choice = choice_window()
    choice.show()
    sys.exit(app.exec_())


    
        