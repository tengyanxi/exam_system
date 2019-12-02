import json
from get_data import get_data
import random


class Question:
    def __init__(self, id_, num):
        global wrong_questions
        self._id = id_  # 该题型的id号
        self._num = num  # 该题型的数量
        try:
            self._extract_questions = random.sample(get_data(id_), self._num)  # 抽取满足id号的所有num道题目
        except:
            self._num = len(get_data(id_))
            self._extract_questions = random.sample(get_data(id_), self._num)
        self._eachScore = 1  # 该题型每题的分数
        self._score = 0  # 该题型初始的得分为0分
        self._answers = {}  # 存放选取的答案的一个字典，每次点击上一题/下一题按钮时就更新
        self._question_id_list = {}  # 将字典的键存入一个列表中，避免多次在extract_questions中查找
        self.init_answers()
        self.init_star()

    def init_answers(self):  # 初始化存放答案的字典及存放键的列表，值都设为空
        for i in range(self._num):
            self._question_id_list[i] = self._extract_questions[i][-1]
            a = self._extract_questions[i][-3].replace(" ","")
            self._answers[i] = [a, '']
        print(self._question_id_list)

    def init_star(self):
        try:
            with open("star.json", "r") as f:
                self._starData = json.load(f)
        except:
            self._starData = {}

    def add_answer(self, qid, your_answer):  # 将选择的答案先记录
        self._answers[qid][1] = your_answer
        print(self._answers)

    def calculate_score(self):  # 点击交卷按钮时调用该函数
        try:
            with open("wrong_question.json", "r") as f:
                wrongData = json.load(f)
        except:
            wrongData = {}
        for qid, a in self._answers.items():
            if a[0] == a[1]:
                self._score += self._eachScore
            else:
                wrongData[self._question_id_list[qid]] = self._question_id_list[qid]
            with open('wrong_question.json', 'w') as f:
                json_data = json.dumps(wrongData)
                f.write(json_data)

    def check_answer(self, id_, front=0):
        question_answer = self._answers[id_ - front][0]
        your_answer = self._answers[id_ - front][1]
        if question_answer == your_answer:
            return True, question_answer
        else:
            return False, question_answer

    def if_stared(self, qid):
        if self._question_id_list[qid] in self._starData:
            return True
        return False

    def star(self, qid):
        self.init_star()
        with open('star.json', 'w') as f2:
            self._starData[self._question_id_list[qid]] = self._question_id_list[qid]
            json_data = json.dumps(self._starData)
            f2.write(json_data)
        print(self._starData)

    def cancel_star(self, qid):
        self.init_star()
        with open('star.json', 'w') as f2:
            if self._question_id_list[qid] in self._starData:
                del self._starData[self._question_id_list[qid]]
            json_data = json.dumps(self._starData)
            f2.write(json_data)

    '''def get_answers(self):  # 答案的对外接口
        return self._answers'''

    def get_num(self):  # 题目数量的对外接口
        return self._num

    def get_score(self):  # 该题型所得分数的对外接口
        return self._score


class SingleChoice(Question):
    def __init__(self, id_, num):
        super().__init__(id_, num)

    def show_problem(self, qid, front=0):
        question = self._extract_questions[qid]
        return str(qid + front + 1) + '.' + question[0] + '  （难易度：' + question[-2] + '）' + '\n' + 'A：' + question[1] \
               + '\n' + 'B：' + question[2] + '\n' + 'C：' + question[3] + '\n' + 'D：' + question[4] + '\n'


class MultipleChoice(SingleChoice):
    def __init__(self, id_, num):
        super().__init__(id_, num)
        self._eachScore = 2


class JudgmentQuestion(Question):
    def __init__(self, id_, num):
        super().__init__(id_, num)

    def show_problem(self, qid, front=0):
        question = self._extract_questions[qid]
        return str(qid + front + 1) + '.' + question[0] + '  （难易度：' + question[-2] + '）' + '\n'
