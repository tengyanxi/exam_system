import sys
import json
from select_window import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from add_elem import *

class select(Ui_MainWindow,QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()
    
    def initUi(self):
        self.button_addfile.clicked.connect(self.button_addfile_click)
        self.button_exam.clicked.connect(self.button_exam_click)
        self.button_exercise.clicked.connect(self.button_exercise_click)
        self.button_wrong.clicked.connect(self.buttton_wrong_click)

    def button_addfile_click(self):
        fileName,filetype = QFileDialog.getOpenFileName(self,"选择文件","./", "All Files(*)")
        #decide_type()
    
    '''def decide_type(self, fileName):
        possible_type = [".json"]
        for i in possible_type:
            if i in fileName:
                #定义一个函数，将符合格式的文件转化为json文件类型，返回值为json文件名
                pass'''
    def button_exam_click(self):
        pass

    def button_exercise_click(self):
        choice.show()

    def buttton_wrong_click(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    selected_window = select()
    selected_window.show()
    choice = choice_window()
    sys.exit(app.exec_())