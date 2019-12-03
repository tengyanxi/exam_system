import json
import sys
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from exercise_window import Ui_ExerciseWindow
from question_types import SingleChoice, MultipleChoice, JudgmentQuestion

lessons = {"马原": "0","近代史": "1", "思修": "2"}
questionType = {"单选": "1", "多选": '2', "判断": '0'}


class Exercise(Ui_ExerciseWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._yourAnswer = ""  # 存放每次选择的答案
        self._yourAnswers = {}  # 记录选择的答案，用于回溯到做过的题目时恢复选项框状态
        self._currentQid = 0  # 记录当前题号，从0开始计数
        self.init_q_n()
        self._singleChoice = SingleChoice(self.q1, self.n1)
        self._multipleChoice = MultipleChoice(self.q2, self.n2)
        self._judgmentQuestion = JudgmentQuestion(self.q3, self.n3)
        self.n1 = self._singleChoice.get_num()  # 防止题目数量超出导致n的改变
        self.n2 = self._multipleChoice.get_num()
        self.n3 = self._judgmentQuestion.get_num()
        self.initUi()
        self.init_choose()
        self.init_your_answers()
        self.setFixedSize(self.width(), self.height())  # 固定窗口大小
        self.setWindowModality(Qt.ApplicationModal)

    def init_q_n(self):
        with open("exam_number.json", "r") as f2:
            exam_number = json.load(f2)
        self.n1 = exam_number["Single"]
        self.n2 = exam_number["Multiple"]
        self.n3 = exam_number["Judge"]
        self.q1 = lessons["马原"] + questionType["单选"]
        self.q2 = lessons["马原"] + questionType["多选"]
        self.q3 = lessons["马原"] + questionType["判断"]


    def initUi(self):
        self.checkBox.setHidden(True)
        self.checkBox_2.setHidden(True)
        self.checkBox_3.setHidden(True)
        self.checkBox_4.setHidden(True)
        self.radioButton_5.setHidden(True)
        self.radioButton_6.setHidden(True)
        self.radioButton_7.setHidden(True)  # 始终存在一个隐藏的单选框，切换到未做的题目时使其checked
        txt = self._singleChoice.show_problem(0)  # 初始化第一道选择题的题目
        self.textEdit.setText(txt)
        self.push_button_is_enabled()  # 第一时不能按上一题的按钮
        self.stared_or_not(self._singleChoice.if_stared(0))
        self.pushButton.clicked.connect(self.show1)
        self.pushButton_2.clicked.connect(self.show2)
        self.pushButton_3.clicked.connect(self.check_)
        self.pushButton_4.clicked.connect(self.star_or_cancel)

    def init_choose(self):
        for i in range(self.n1 + self.n2 + self.n3):
            self.listWidget.addItem("第" + str(i + 1) + "题")
        self.listWidget.itemDoubleClicked.connect(self.switch_question)
        self.listWidget.setCurrentRow(self._currentQid)  # 一开始选中第一题

    def init_your_answers(self):  # 初始化做题者的答案的字典，初始值都设为空，这样做题者只要没答某道题，返回该题时自动恢复未选择状态
        for i in range(self.n1 + self.n2 + self.n3):
            self._yourAnswers[i] = ''

    def push_button_is_enabled(self):
        # 第一题不能按 上一题 的按钮
        if self._currentQid == 0:
            self.pushButton.setEnabled(False)
        else:
            self.pushButton.setEnabled(True)
        # 最后一题不能按 下一题 的按钮
        if self._currentQid == self.n1 + self.n2 + self.n3 - 1:
            self.pushButton_2.setEnabled(False)
        else:
            self.pushButton_2.setEnabled(True)

    def object_change1(self):  # 单选转多选
        self.radioButton.setHidden(True)
        self.radioButton_2.setHidden(True)
        self.radioButton_3.setHidden(True)
        self.radioButton_4.setHidden(True)
        self.checkBox.setHidden(False)
        self.checkBox_2.setHidden(False)
        self.checkBox_3.setHidden(False)
        self.checkBox_4.setHidden(False)

    def object_change2(self):  # 多选转单选
        self.radioButton.setHidden(False)
        self.radioButton_2.setHidden(False)
        self.radioButton_3.setHidden(False)
        self.radioButton_4.setHidden(False)
        self.checkBox.setHidden(True)
        self.checkBox_2.setHidden(True)
        self.checkBox_3.setHidden(True)
        self.checkBox_4.setHidden(True)

    def object_change3(self):  # 多选转判断
        self.checkBox.setHidden(True)
        self.checkBox_2.setHidden(True)
        self.checkBox_3.setHidden(True)
        self.checkBox_4.setHidden(True)
        self.radioButton_5.setHidden(False)
        self.radioButton_6.setHidden(False)

    def object_change4(self):  # 判断转多选
        self.checkBox.setHidden(False)
        self.checkBox_2.setHidden(False)
        self.checkBox_3.setHidden(False)
        self.checkBox_4.setHidden(False)
        self.radioButton_5.setHidden(True)
        self.radioButton_6.setHidden(True)

    def object_change5(self):  # 单选转判断
        self.radioButton.setHidden(True)
        self.radioButton_2.setHidden(True)
        self.radioButton_3.setHidden(True)
        self.radioButton_4.setHidden(True)
        self.radioButton_5.setHidden(False)
        self.radioButton_6.setHidden(False)

    def object_change6(self):  # 判断转单选
        self.radioButton.setHidden(False)
        self.radioButton_2.setHidden(False)
        self.radioButton_3.setHidden(False)
        self.radioButton_4.setHidden(False)
        self.radioButton_5.setHidden(True)
        self.radioButton_6.setHidden(True)

    def set_answer1(self):  # 设置单选题选择按钮状态
        if self.radioButton.isChecked():
            self._yourAnswer = 'A'
        elif self.radioButton_2.isChecked():
            self._yourAnswer = 'B'
        elif self.radioButton_3.isChecked():
            self._yourAnswer = 'C'
        elif self.radioButton_4.isChecked():
            self._yourAnswer = 'D'
        else:
            self._yourAnswer = ''

    def set_answer2(self):  # 设置多选题选择按钮状态
        self._yourAnswer = ''
        if self.checkBox.isChecked():
            self._yourAnswer += 'A'
        if self.checkBox_2.isChecked():
            self._yourAnswer += 'B'
        if self.checkBox_3.isChecked():
            self._yourAnswer += 'C'
        if self.checkBox_4.isChecked():
            self._yourAnswer += 'D'

    def set_answer3(self):  # 设置判断题选择按钮状态
        if self.radioButton_5.isChecked():
            self._yourAnswer = 'Y'
        elif self.radioButton_6.isChecked():
            self._yourAnswer = 'N'
        else:
            self._yourAnswer = ''

    def return_answer1(self, id_):  # 返回单选题所选的选项
        answer = self._yourAnswers[id_]
        if answer == 'A':
            self.radioButton.setChecked(True)
        elif answer == 'B':
            self.radioButton_2.setChecked(True)
        elif answer == 'C':
            self.radioButton_3.setChecked(True)
        elif answer == 'D':
            self.radioButton_4.setChecked(True)
        else:
            self.radioButton_7.setChecked(True)

    def return_answer2(self, id_):  # 返回多选题所选的选项
        answer = self._yourAnswers[id_]
        self.checkBox.setChecked(False)  # 先清空选项
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        if answer.find('A') != -1:
            self.checkBox.setChecked(True)
        if answer.find('B') != -1:
            self.checkBox_2.setChecked(True)
        if answer.find('C') != -1:
            self.checkBox_3.setChecked(True)
        if answer.find('D') != -1:
            self.checkBox_4.setChecked(True)

    def return_answer3(self, id_):  # 返回判断题所选的选项
        answer = self._yourAnswers[id_]
        self.radioButton_7.setChecked(True)
        if answer == 'Y':
            self.radioButton_5.setChecked(True)
        elif answer == 'N':
            self.radioButton_6.setChecked(True)

    def skip(self, item):
        if item < self.n1:  # 如果选中的是单选题
            self.object_change2()
            self.object_change6()
            txt = self._singleChoice.show_problem(item)
            self.textEdit.setText(txt)
            self.return_answer1(item)
            self.stared_or_not(self._singleChoice.if_stared(item))
        elif item < self.n1 + self.n2:  # 如果选中的是多选题
            self.object_change1()
            self.object_change4()
            front = self.n1
            txt = self._multipleChoice.show_problem(item - front, front)
            self.textEdit.setText(txt)
            self.return_answer2(item)
            self.stared_or_not(self._multipleChoice.if_stared(item - front))
        else:  # 如果选中的是判断题
            self.object_change3()
            self.object_change5()
            front = self.n1 + self.n2
            txt = self._judgmentQuestion.show_problem(item - front, front)
            self.textEdit.setText(txt)
            self.return_answer3(item)
            self.stared_or_not(self._judgmentQuestion.if_stared(item - front))

    def switch_question(self):
        indexes = self.listWidget.selectedIndexes()
        item = int(indexes[0].row())
        if self._currentQid < self.n1:   # 当前停留在单选题
            self.set_answer1()
            self._singleChoice.add_answer(self._currentQid, self._yourAnswer)
            self.skip(item)
        elif self._currentQid < self.n1 + self.n2:   # 当前停留在多选题
            self.set_answer2()
            self._multipleChoice.add_answer(self._currentQid - self.n1, self._yourAnswer)
            self.skip(item)
        else:  # 当前停留在判断题
            self.set_answer3()
            self._judgmentQuestion.add_answer(self._currentQid - self.n1 - self.n2, self._yourAnswer)
            self.skip(item)
        self._yourAnswers[self._currentQid] = self._yourAnswer
        self._currentQid = item  # 及时更新当前所在题号
        self.push_button_is_enabled()

    def show1(self):  # 切换至上一题
        # 单选题切换到单选题的上一题
        if self._currentQid < self.n1:
            qid = self._currentQid
            self.set_answer1()
            self._singleChoice.add_answer(qid, self._yourAnswer)
            txt = self._singleChoice.show_problem(qid - 1)
            self.textEdit.setText(txt)
            self.return_answer1(qid - 1)
            self.stared_or_not(self._singleChoice.if_stared(qid - 1))
        # 多选题的第一题切换到单选题的最后一题
        elif self._currentQid == self.n1:
            qid = self._currentQid
            self.set_answer2()
            self.object_change2()
            self._multipleChoice.add_answer(0, self._yourAnswer)
            txt = self._singleChoice.show_problem(qid - 1)
            self.textEdit.setText(txt)
            self.return_answer1(qid - 1)
            self.stared_or_not(self._singleChoice.if_stared(qid - 1))
        # 多选题切换到多选题的上一题
        elif self._currentQid < self.n1 + self.n2:
            front = self.n1
            qid = self._currentQid - front
            self.set_answer2()
            self._multipleChoice.add_answer(qid, self._yourAnswer)
            txt = self._multipleChoice.show_problem(qid - 1, front)
            self.textEdit.setText(txt)
            self.return_answer2(self._currentQid - 1)
            self.stared_or_not(self._multipleChoice.if_stared(self._currentQid - 1 - front))
        # 判断题的第一题切换到多选题的最后一题
        elif self._currentQid == self.n1 + self.n2:
            front = self.n1
            qid = self._currentQid - front
            self.set_answer3()
            self.object_change4()
            self._judgmentQuestion.add_answer(0, self._yourAnswer)
            txt = self._multipleChoice.show_problem(qid - 1, front)
            self.textEdit.setText(txt)
            self.return_answer2(self._currentQid - 1)
            self.stared_or_not(self._multipleChoice.if_stared(self._currentQid - 1 - front))
        # 判断题切换到判断题的上一题
        else:
            front = self.n1 + self.n2
            qid = self._currentQid - front
            self.set_answer3()
            self._judgmentQuestion.add_answer(qid, self._yourAnswer)
            txt = self._judgmentQuestion.show_problem(qid - 1, front)
            self.textEdit.setText(txt)
            self.return_answer3(self._currentQid - 1)
            self.stared_or_not(self._judgmentQuestion.if_stared(self._currentQid - 1 - front))
        self._yourAnswers[self._currentQid] = self._yourAnswer
        self._currentQid -= 1
        self.listWidget.setCurrentRow(self._currentQid)  # 设置列表框里的列表随着按上一题/下一题的按钮及时更新
        self.push_button_is_enabled()  # 每次切换题目时都判断按钮可用性

    def show2(self):  # 切换至下一题
        # 单选题切换到单选题的下一题
        if self._currentQid < self.n1 - 1:
            qid = self._currentQid
            self.set_answer1()
            self._singleChoice.add_answer(qid, self._yourAnswer)
            txt = self._singleChoice.show_problem(qid + 1)
            self.textEdit.setText(txt)
            self.return_answer1(self._currentQid + 1)
            self.stared_or_not(self._singleChoice.if_stared(qid + 1))
        # 单选题的最后一题切换到多选题的第一题
        elif self._currentQid == self.n1 - 1:
            front = self.n1
            qid = self._currentQid - front
            self.set_answer1()
            self.object_change1()
            self._singleChoice.add_answer(front - 1, self._yourAnswer)
            txt = self._multipleChoice.show_problem(qid + 1, front)
            self.textEdit.setText(txt)
            self.return_answer2(self._currentQid + 1)
            self.stared_or_not(self._multipleChoice.if_stared(self._currentQid + 1 - front))
        # 多选题切换到多选题的下一题
        elif self._currentQid < self.n1 + self.n2 - 1:
            front = self.n1
            qid = self._currentQid - front
            self.set_answer2()
            self._multipleChoice.add_answer(qid, self._yourAnswer)
            txt = self._multipleChoice.show_problem(qid + 1, front)
            self.textEdit.setText(txt)
            self.return_answer2(self._currentQid + 1)
            self.stared_or_not(self._multipleChoice.if_stared(self._currentQid + 1 - front))
        # 多选题的最后一题切换到判断题的第一题
        elif self._currentQid == self.n1 + self.n2 - 1:
            front = self.n1 + self.n2
            qid = self._currentQid - front
            self.set_answer2()
            self.object_change3()
            self._multipleChoice.add_answer(self.n2 - 1, self._yourAnswer)
            txt = self._judgmentQuestion.show_problem(qid + 1, front)
            self.textEdit.setText(txt)
            self.return_answer3(self._currentQid + 1)
            self.stared_or_not(self._judgmentQuestion.if_stared(self._currentQid + 1 - front))
        # 判断题切换到判断题的下一题
        else:
            front = self.n1 + self.n2
            qid = self._currentQid - front
            self.set_answer3()
            self._judgmentQuestion.add_answer(qid, self._yourAnswer)
            txt = self._judgmentQuestion.show_problem(qid + 1, front)
            self.textEdit.setText(txt)
            self.return_answer3(self._currentQid + 1)
            self.stared_or_not(self._judgmentQuestion.if_stared(self._currentQid + 1 - front))
        self._yourAnswers[self._currentQid] = self._yourAnswer
        self._currentQid += 1
        self.listWidget.setCurrentRow(self._currentQid)
        self.push_button_is_enabled()

    def check_(self):
        if self._currentQid < self.n1:
            self.set_answer1()
            self._singleChoice.add_answer(self._currentQid, self._yourAnswer)
            bool_, s = self._singleChoice.check_answer(self._currentQid)
            if not bool_:
                QMessageBox.information(self, '错误', '答案错误，正确答案为：' + s)
                self.listWidget.item(self._currentQid).setBackground(QColor("red"))
            else:
                QMessageBox.information(self, '正确', '答案正确')
                self.listWidget.item(self._currentQid).setBackground(QColor("green"))
        elif self._currentQid < self.n1 + self.n2:
            self.set_answer2()
            self._multipleChoice.add_answer(self._currentQid - self.n1, self._yourAnswer)
            bool_, s = self._multipleChoice.check_answer(self._currentQid, self.n1)
            if not bool_:
                QMessageBox.information(self, '错误', '答案错误，正确答案为：' + s)
                self.listWidget.item(self._currentQid).setBackground(QColor("red"))
            else:
                QMessageBox.information(self, '正确', '答案正确')
                self.listWidget.item(self._currentQid).setBackground(QColor("green"))
        else:
            self.set_answer3()
            self._judgmentQuestion.add_answer(self._currentQid - self.n1 - self.n2, self._yourAnswer)
            bool_, s = self._judgmentQuestion.check_answer(self._currentQid, self.n1 + self.n2)
            if not bool_:
                QMessageBox.information(self, '错误', '答案错误，正确答案为：' + s)
                self.listWidget.item(self._currentQid).setBackground(QColor("red"))
            else:
                QMessageBox.information(self, '正确', '答案正确')
                self.listWidget.item(self._currentQid).setBackground(QColor("green"))

    def stared_or_not(self, bool_):
        if bool_:
            self.pushButton_4.setText("已收藏")
        else:
            self.pushButton_4.setText("收藏")

    def star_or_cancel(self):    # 收藏或者取消收藏功能
        if self._currentQid < self.n1:
            if self.pushButton_4.text() == "已收藏":
                self.pushButton_4.setText("收藏")
                self._singleChoice.cancel_star(self._currentQid)
            else:
                self.pushButton_4.setText("已收藏")
                self._singleChoice.star(self._currentQid)
        elif self._currentQid < self.n1 + self.n2:
            if self.pushButton_4.text() == "已收藏":
                self.pushButton_4.setText("收藏")
                self._multipleChoice.cancel_star(self._currentQid - self.n1)
            else:
                self.pushButton_4.setText("已收藏")
                self._multipleChoice.star(self._currentQid - self.n1)
        else:
            if self.pushButton_4.text() == "已收藏":
                self.pushButton_4.setText("收藏")
                self._judgmentQuestion.cancel_star(self._currentQid - self.n1 - self.n2)
            else:
                self.pushButton_4.setText("已收藏")
                self._judgmentQuestion.star(self._currentQid - self.n1 - self.n2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mockTestWindow = Exercise()
    mockTestWindow.show()
    sys.exit(app.exec_())
