from get_data import get_data
import random

wrong_questions = set()  # 错题集（收录错题的id号），以集合方式存放避免重复

class Question:
    def __init__(self, id_, num):
        global wrong_questions
        self._id = id_  # 该题型的id号
        self._num = num  # 该题型的数量
        self._extract_questions = random.sample(get_data(id_), self._num)  # 抽取满足id号的所有num道题目
        self._eachScore = 1  # 该题型每题的分数
        self._score = 0  # 该题型初始的得分为0分
        self._answers = {}  # 存放选取的答案的一个字典，每次点击上一题/下一题按钮时就更新
        self._answers_list = []  # 将字典的键存入一个列表中，避免多次在extract_questions中查找
        self.init_answers()

    def init_answers(self):  # 初始化存放答案的字典及存放键的列表，值都设为空
        for i in range(self._num):
            self._answers_list.append(str(i) + self._extract_questions[i][-3])
            self._answers[self._answers_list[i]] = ''

    def add_answer(self, qid, your_answer):  # 将选择的答案先记录
        self._answers[self._answers_list[qid]] = your_answer
        print(self._answers)

    def calculate_score(self):  # 点击交卷按钮时调用该函数
        for question_answer, your_answer in self._answers.items():
            s = "".join([a for a in question_answer if a.isalpha()])
            if s == your_answer:
                self._score += self._eachScore
            '''else:
                wrong_questions.add()'''

    def get_answers(self):  # 答案的对外接口
        return self._answers

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