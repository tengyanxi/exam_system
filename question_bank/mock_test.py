import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from mock_test_window import Ui_MockTestWindow
from question_types import SingleChoice, MultipleChoice, JudgmentQuestion

lessons = {"马原": "0"}
questionType = {"单选": "1", "多选": '2', "判断": '0'}


class MockTest(Ui_MockTestWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._yourAnswer = ""  # 存放每次选择的答案
        self._yourAnswers = {}  # 记录选择的答案，用于回溯到做过的题目时恢复选项框状态
        self._currentQid = 0  # 记录当前题号，从0开始计数
        self._singleChoice = SingleChoice(lessons["马原"] + questionType["单选"], 10)
        self._multipleChoice = MultipleChoice(lessons["马原"] + questionType["多选"], 10)
        self._judgmentQuestion = JudgmentQuestion(lessons["马原"] + questionType["判断"], 10)
        self.initUi()
        self.init_time()
        self.init_choose()
        self.init_your_answers()

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
        self.pushButton.clicked.connect(self.show1)
        self.pushButton_2.clicked.connect(self.show2)
        self.pushButton_3.clicked.connect(self.send)

    def init_time(self):  # 倒计时功能
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self._minute = 89
        self._second = 60
        self.timer.timeout.connect(self.time_change)

    def init_choose(self):
        for i in range(self._singleChoice.get_num() + self._multipleChoice.get_num() + self._judgmentQuestion.get_num()):
            self.listWidget.addItem("第" + str(i + 1) + "题")
        self.listWidget.itemDoubleClicked.connect(self.switch_question)

    def init_your_answers(self):  # 初始化做题者的答案的字典，初始值都设为空，这样做题者只要没答某道题，返回该题时自动恢复未选择状态
        for i in range(
                self._singleChoice.get_num() + self._multipleChoice.get_num() + self._judgmentQuestion.get_num()):
            self._yourAnswers[i] = ''

    def time_change(self):
        self._second -= 1
        if self._second == 0 and self._minute > 0:
            self._minute -= 1
            self._second = 59
        self.label.setText('{:0>2d}:{:0>2d}'.format(self._minute, self._second))
        if self._second == 0 and self._minute == 0:
            self.timer.stop()


    def push_button_is_enabled(self):
        # 第一题不能按 上一题 的按钮
        if self._currentQid == 0:
            self.pushButton.setEnabled(False)
        else:
            self.pushButton.setEnabled(True)
        # 最后一题不能按 下一题 的按钮
        if self._currentQid == self._singleChoice.get_num() + self._multipleChoice.get_num() + \
                self._judgmentQuestion.get_num() - 1:
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
        if item < self._singleChoice.get_num():  # 如果选中的是单选题
            self.object_change2()
            self.object_change6()
            txt = self._singleChoice.show_problem(item)
            self.textEdit.setText(txt)
            self.return_answer1(item)
            print(self._yourAnswers[item])
        elif item < self._singleChoice.get_num() + self._multipleChoice.get_num():  # 如果选中的是多选题
            self.object_change1()
            self.object_change4()
            front = self._singleChoice.get_num()
            txt = self._multipleChoice.show_problem(item - front, front)
            self.textEdit.setText(txt)
            self.return_answer2(item)
        else:  # 如果选中的是判断题
            self.object_change3()
            self.object_change5()
            front = self._singleChoice.get_num() + self._multipleChoice.get_num()
            txt = self._multipleChoice.show_problem(item - front, front)
            self.textEdit.setText(txt)
            self.return_answer3(item)

    def switch_question(self):
        indexes = self.listWidget.selectedIndexes()
        for b in indexes:
            item = int(b.row())
            #print(item)
        if self._currentQid < self._singleChoice.get_num():   # 当前停留在单选题
            self.set_answer1()
            self._singleChoice.add_answer(self._currentQid, self._yourAnswer)
            self.skip(item)
        elif self._currentQid < self._singleChoice.get_num() + self._multipleChoice.get_num():   # 当前停留在多选题
            self.set_answer2()
            self._multipleChoice.add_answer(self._currentQid - self._singleChoice.get_num(), self._yourAnswer)
            self.skip(item)
        else:  # 当前停留在判断题
            self.set_answer3()
            self._judgmentQuestion.add_answer(self._currentQid - self._singleChoice.get_num() - self._multipleChoice.get_num(), self._yourAnswer)
            self.skip(item)
        self._yourAnswers[self._currentQid] = self._yourAnswer
        self._currentQid = item
        self.push_button_is_enabled()

    def show1(self):  # 切换至上一题
        # 单选题切换到单选题的上一题
        if self._currentQid < self._singleChoice.get_num():
            qid = self._currentQid
            self.set_answer1()
            self._singleChoice.add_answer(qid, self._yourAnswer)
            txt = self._singleChoice.show_problem(qid - 1)
            self.textEdit.setText(txt)
            self.return_answer1(qid - 1)
        # 多选题的第一题切换到单选题的最后一题
        elif self._currentQid == self._singleChoice.get_num():
            qid = self._currentQid
            self.set_answer2()
            self.object_change2()
            self._multipleChoice.add_answer(0, self._yourAnswer)
            txt = self._singleChoice.show_problem(qid - 1)
            self.textEdit.setText(txt)
            self.return_answer1(self._currentQid - 1)
        # 多选题切换到多选题的上一题
        elif self._currentQid < self._singleChoice.get_num() + self._multipleChoice.get_num():
            front = self._singleChoice.get_num()
            qid = self._currentQid - front
            self.set_answer2()
            self._multipleChoice.add_answer(qid, self._yourAnswer)
            txt = self._multipleChoice.show_problem(qid - 1, front)
            self.textEdit.setText(txt)
            self.return_answer2(self._currentQid - 1)
        # 判断题的第一题切换到多选题的最后一题
        elif self._currentQid == self._singleChoice.get_num() + self._multipleChoice.get_num():
            front = self._singleChoice.get_num()
            qid = self._currentQid - front
            self.set_answer3()
            self.object_change4()
            self._judgmentQuestion.add_answer(0, self._yourAnswer)
            txt = self._multipleChoice.show_problem(qid - 1, front)
            self.textEdit.setText(txt)
            self.return_answer2(self._currentQid - 1)
        # 判断题切换到判断题的上一题
        else:
            front = self._singleChoice.get_num() + self._multipleChoice.get_num()
            qid = self._currentQid - front
            self.set_answer3()
            self._judgmentQuestion.add_answer(qid, self._yourAnswer)
            txt = self._judgmentQuestion.show_problem(qid - 1, front)
            self.textEdit.setText(txt)
            self.return_answer3(self._currentQid - 1)
        self._yourAnswers[self._currentQid] = self._yourAnswer
        self._currentQid -= 1
        self.push_button_is_enabled()  # 每次切换题目时都判断按钮可用性

    def show2(self):  # 切换至下一题
        # 单选题切换到单选题的下一题
        if self._currentQid < self._singleChoice.get_num() - 1:
            qid = self._currentQid
            self.set_answer1()
            self._singleChoice.add_answer(qid, self._yourAnswer)
            txt = self._singleChoice.show_problem(qid + 1)
            self.textEdit.setText(txt)
            self.return_answer1(self._currentQid + 1)
        # 单选题的最后一题切换到多选题的第一题
        elif self._currentQid == self._singleChoice.get_num() - 1:
            front = self._singleChoice.get_num()
            qid = self._currentQid - front
            self.set_answer1()
            self.object_change1()
            self._singleChoice.add_answer(front - 1, self._yourAnswer)
            txt = self._multipleChoice.show_problem(qid + 1, front)
            self.textEdit.setText(txt)
            self.return_answer2(self._currentQid + 1)
        # 多选题切换到多选题的下一题
        elif self._currentQid < self._singleChoice.get_num() + self._multipleChoice.get_num() - 1:
            front = self._singleChoice.get_num()
            qid = self._currentQid - front
            self.set_answer2()
            self._multipleChoice.add_answer(qid, self._yourAnswer)
            txt = self._multipleChoice.show_problem(qid + 1, front)
            self.textEdit.setText(txt)
            self.return_answer2(self._currentQid + 1)
        # 多选题的最后一题切换到判断题的第一题
        elif self._currentQid == self._singleChoice.get_num() + self._multipleChoice.get_num() - 1:
            front = self._singleChoice.get_num() + self._multipleChoice.get_num()
            qid = self._currentQid - front
            self.set_answer2()
            self.object_change3()
            self._multipleChoice.add_answer(self._multipleChoice.get_num() - 1, self._yourAnswer)
            txt = self._judgmentQuestion.show_problem(qid + 1, front)
            self.textEdit.setText(txt)
            self.return_answer3(self._currentQid + 1)
        # 判断题切换到判断题的下一题
        else:
            front = self._singleChoice.get_num() + self._multipleChoice.get_num()
            qid = self._currentQid - front
            self.set_answer3()
            self._judgmentQuestion.add_answer(qid, self._yourAnswer)
            txt = self._judgmentQuestion.show_problem(qid + 1, front)
            self.textEdit.setText(txt)
            self.return_answer3(self._currentQid + 1)
        self._yourAnswers[self._currentQid] = self._yourAnswer
        self._currentQid += 1
        self.push_button_is_enabled()

    def add_last_answer(self):  # 可能会有中途交卷的情况发生，需要将当前页面上的答案录入答案字典
        if self._currentQid < self._singleChoice.get_num():
            self.set_answer1()
            self._singleChoice.add_answer(self._currentQid, self._yourAnswer)
        elif self._currentQid < self._singleChoice.get_num() + self._multipleChoice.get_num():
            self.set_answer2()
            self._multipleChoice.add_answer(self._currentQid - self._singleChoice.get_num(), self._yourAnswer)
        else:
            self.set_answer3()
            self._judgmentQuestion.add_answer(
                self._currentQid - self._singleChoice.get_num() - self._multipleChoice.get_num(), self._yourAnswer)

    def calculate_total_score(self):  # 计算总的得分
        self._singleChoice.calculate_score()
        self._multipleChoice.calculate_score()
        self._judgmentQuestion.calculate_score()
        return self._singleChoice.get_score() + self._multipleChoice.get_score() + self._judgmentQuestion.get_score()

    def send(self):  # 交卷并评分
        reply = QMessageBox.question(self, '提示', '确认要交卷吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply:
            self.add_last_answer()
            score = self.calculate_total_score()
            reply2 = QMessageBox.information(self, '得分', '您的得分为：' + str(score) + '分')
            if reply2:
                self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mockTestWindow = MockTest()
    mockTestWindow.show()
    sys.exit(app.exec_())
