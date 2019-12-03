import sys,random,json
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from select_window import *
from PyQt5 import QtWidgets
from mock_test import MockTest
from exercise import Exercise
from choice_function import ChoiceType


class select(Ui_MainWindow,QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()
        self.setFixedSize(self.width(), self.height())
        self.radioButton_2.setEnabled(False)
        self.radioButton_3.setEnabled(False)

    def radiobutton_my_click(self):
        with open("data.json", encoding = "UTF-8") as f:
            data = json.load(f)
        question = {}
        for key in data.keys():
            if key[0] == "0":
                question[key] = data[key]
        with open("questions.json", "w") as f:
            json.dump(question, f)


    def radiobutton_jds_click(self):
        with open("data.json", encoding = "UTF-8") as f:
            data = json.load(f)
        question = {}
        for key in data.keys():
            if key[0] == "1":
                question[key] = data[key]
        with open("questions.json", "w") as f:
            json.dump(question, f)

    
    def radiobutton_sx_click(self):
        with open("data.json", encoding = "UTF-8") as f:
            data = json.load(f)
        question = {}
        for key in data.keys():
            if key[0] == "2":
                question[key] = data[key]
        with open("questions.json", "w") as f:
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
        if not (self.radioButton.isChecked() or self.radioButton_2.isChecked() or self.radioButton_3.isChecked()):
            QMessageBox.information(self, "错误提示", "请先选择科目！")
        else:
            question = {}
            question["Judge"] = 20000
            question["Single"] = 20000
            question["Multiple"] = 10000
            with open("exam_number.json", "w") as f:
                json.dump(question, f)
            try:
                with open ("star.json") as f:
                    star = json.load(f)
            except:
                with open ("star.json", 'w') as f:
                    star = {'00010001': '00010001', "01010002": "01010002", "02010001": "02010001"}
                    json.dump(star, f)
            with open("questions.json") as file:
                data = json.load(file)
            questions = {}
            n = ''
            for key in star.keys():
                questions[key] = data[key]
                if '00' in key[0:2]:
                    n += 'a'
                elif '01' in key[0:2]:
                    n += 'b'
                elif '02' in key[0:2]:
                    n += 'c'
            flag = True
            if 'a' not in n:
                questions['00010001'] = data['00010001']
                flag = False
            if 'b' not in n:
                questions["01010002"] = data["01010002"]
                flag = False
            if 'c' not in n:
                questions["02010001"] = data["02010001"]
                flag = False
            if flag == False:
                with open ("star.json", 'w') as f:
                    star['00010001'] = '00010001'
                    star["01010002"] = "01010002"
                    star["02010001"] = "02010001"
                    json.dump(star, f)
            with open ("exam_bank.json", "w") as f:
                json.dump(questions, f)
            self.e3 = Exercise()
            self.e3.show()

    def button_exam_click(self):
        if not (self.radioButton.isChecked() or self.radioButton_2.isChecked() or self.radioButton_3.isChecked()):
            QMessageBox.information(self, "错误提示", "请先选择科目！")
        else:
            single_num = 20
            several_num = 10
            decide_num = 20
            with open("questions.json") as file:
                data = json.load(file)
            questions = {}
            question = {}
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
                single_question.remove(''.join(q))
                questions[q[0]] = data[q[0]]
            for i in range(several_num):
                q = random.choices(several_question)
                several_question.remove(''.join(q))
                questions[q[0]] = data[q[0]]
            for i in range(decide_num):
                q = random.choices(decide_question)
                decide_question.remove(''.join(q))
                questions[q[0]] = data[q[0]]
            question["Judge"] = 20
            question["Single"] = 20
            question["Multiple"] = 10
            with open ("exam_bank.json", "w") as f:
                json.dump(questions, f)
            with open ("exam_number.json", "w") as f1:
                json.dump(question, f1)
            self.t = MockTest()
            self.t.show()

    def button_exercise_click(self):
        if not (self.radioButton.isChecked() or self.radioButton_2.isChecked() or self.radioButton_3.isChecked()):
            QMessageBox.information(self, "错误提示", "请先选择科目！")
        else:
            self.c = ChoiceType()
            self.c.show()

    def buttton_wrong_click(self):
        if not (self.radioButton.isChecked() or self.radioButton_2.isChecked() or self.radioButton_3.isChecked()):
            QMessageBox.information(self, "错误提示", "请先选择科目！")
        else:
            question = {}
            question["Judge"] = 20000
            question["Single"] = 20000
            question["Multiple"] = 10000
            with open("exam_number.json", "w") as f:
                json.dump(question, f)
            try:
                with open ("wrong_question.json") as f:
                    wrong = json.load(f)
            except:
                with open ("wrong_question.json", 'w') as f:
                    wrong = {'00010001': '00010001', "01010002": "01010002", "02010001": "02010001"}
                    json.dump(wrong, f)
            with open("questions.json") as file:
                data = json.load(file)
            questions = {}
            n = ''
            for key in wrong.keys():
                questions[key] = data[key]
                if '00' in key[0:2]:
                    n += 'a'
                elif '01' in key[0:2]:
                    n += 'b'
                elif '02' in key[0:2]:
                    n += 'c'
            flag = True
            if 'a' not in n:
                questions['00010001'] = data['00010001']
                flag = False
            if 'b' not in n:
                questions["01010002"] = data["01010002"]
                flag = False
            if 'c' not in n:
                questions["02010001"] = data["02010001"]
                flag = False
            if flag == False:
                with open ("wrong_question.json", 'w') as f:
                    wrong['00010001'] = '00010001'
                    wrong["01010002"] = "01010002"
                    wrong["02010001"] = "02010001"
                    json.dump(wrong, f)
            with open ("exam_bank.json", "w") as f:
                json.dump(questions, f)
            self.e2 = Exercise()
            self.e2.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    selected_window = select()
    selected_window.show()
    sys.exit(app.exec_())