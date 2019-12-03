import sys,random,json
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from select_window import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import ChoiceType

class select(Ui_MainWindow,QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()
        
    def radiobutton_my_click(self):
        with open("F:\\match\\my_code\\exam_system\\data.json", encoding = "UTF-8") as f:
            data = json.load(f)
        question = {}
        for key in data.keys():
            if key[0] == "0":
                question[key] = data[key]
        with open("F:\\match\\my_code\\exam_system\\questions.json", "w") as f:
            json.dump(question, f)


    def radiobutton_jds_click(self):
        with open("F:\\match\\my_code\\exam_system\\data.json", encoding = "UTF-8") as f:
            data = json.load(f)
        question = {}
        for key in data.keys():
            if key[0] == "1":
                question[key] = data[key]
        with open("F:\\match\\my_code\\exam_system\\questions.json", "w") as f:
            json.dump(question, f)

    
    def radiobutton_sx_click(self):
        with open("F:\\match\\my_code\\exam_system\\data.json", encoding = "UTF-8") as f:
            data = json.load(f)
        question = {}
        for key in data.keys():
            if key[0] == "2":
                question[key] = data[key]
        with open("F:\\match\\my_code\\exam_system\\questions.json", "w") as f:
            json.dump(question, f)


    def initUi(self):
        self.button_star.clicked.connect(self.button_star_click)
        self.button_exam.clicked.connect(self.button_exam_click)
        self.button_exercise.clicked.connect(self.button_exercise_click)
        self.button_wrong.clicked.connect(self.buttton_wrong_click)
        self.radioButton.toggled.connect(self.radiobutton_my_click)
        self.radioButton_2.toggled.connect(self.radiobutton_jds_click)
        self.radioButton_3.toggled.connect(self.radiobutton_sx_click)
    def button_star_click(self):
        with open ("F:\\match\\my_code\\exam_system\\star.json") as f:
            star = json.load(f)
        with open("F:\\match\\my_code\\exam_system\\questions.json") as file:
            data = json.load(file)
        questions = {}
        for key in star.keys():
            questions[key] = data[key]
        with open ("F:\\match\\my_code\\exam_system\\star.json", "w") as f:
            json.dump(questions, f)

    def button_exam_click(self):
        single_num = 20
        several_num = 10
        decide_num = 20
        with open("F:\\match\\my_code\\exam_system\\questions.json") as file:
            data = json.load(file)
        questions = {}
        single_question = []
        several_question = []
        decide_question = []
        for key in data.keys():
            if key[1] == "1":
                single_question.append(key)
            elif key[1] == "2":
                several_question.append(key)
            elif key[1] == "0":
                decide_question.append(key)
        for i in range(single_num): 
            q = random.choices(single_question)
            questions[q[0]] = data[q[0]]
        for i in range(several_num):
            q = random.choices(several_question)
            questions[q[0]] = data[q[0]]
        for i in range(decide_num):
            q = random.choices(decide_question)
            questions[q[0]] = data[q[0]]
        questions["Judge"] = 20
        questions["Single"] = 20
        questions["Multiple"] = 10
        with open ("F:\\match\\my_code\\exam_system\\exam_bank.json", "w") as f:
            json.dump(questions, f)
        print(questions)
        

    def button_exercise_click(self):
        self.mainWindow = QMainWindow()
        self.ui = ChoiceType.Ui_Dialog()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()

    def buttton_wrong_click(self):
        with open ("F:\\match\\my_code\\exam_system\\wrong_question.json") as f:
            star = json.load(f)
        with open("F:\\match\\my_code\\exam_system\\questions.json") as file:
            data = json.load(file)
        questions = {}
        for key in star.keys():
            questions[key] = data[key]
        with open ("F:\\match\\my_code\\exam_system\\wrong_question.json", "w") as f:
            json.dump(questions, f)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    selected_window = select()
    selected_window.show()
    sys.exit(app.exec_())