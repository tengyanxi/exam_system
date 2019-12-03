import json
import sys
from PyQt5.QtCore import Qt
from ChoiceType import Ui_Dialog
from PyQt5.QtWidgets import QApplication
from matplotlib.backends.backend_qt5 import MainWindow
from question_bank.distribute_questions import distribute_question
from question_bank.exercise import Exercise


class ChoiceType(Ui_Dialog, MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(self.width(), self.height())
        self.setupUi(self)


    def selectionChange(self):
        global d_Judge_num, d_Sgl_num, d_Mul_num
        d_Judge_num = self.comboBox_Judge.currentIndex()
        d_Sgl_num = self.comboBox_Sgl.currentIndex()
        d_Mul_num = self.comboBox_Mul.currentIndex()

    def Continue(self):
        d_type = "012"
        print(distribute_question(d_chap, d_type))
        with open('exam_number.json', 'w', encoding='utf-8') as f1:
            dic = {"Judge": d_Judge_num + 1, "Single": d_Sgl_num + 1, "Multiple": d_Mul_num + 1}
            json.dump(dic, f1, ensure_ascii=False, indent=4)
        with open('exam_bank.json', 'w', encoding='utf-8') as f2:
            seq = []
            dic1 = {}
            dic2 = {}
            for question in distribute_question(d_chap, d_type):
                seq.append(question[-1])
                dic1.update(dic2.fromkeys(seq, question[0:-1]))
                seq = []
                dic2 = {}
            json.dump(dic1, f2, ensure_ascii=False, indent=4)
        self.e = Exercise()
        self.e.show()
        self.close()

    def Exit(self):
        self.close()

    def chapState(self, btn):
        global d_chap
        d_chap = set()
        str_name = "self.Chap0{0}.isChecked()"

        for i in range(0, 8):
            if eval(str_name.format(i)) == 1:
                d_chap.add(str(i))
            else:
                d_chap.discard(str(i))
        d_chap = ''.join(list(d_chap))

    def btnstate(self, btn):
        judge2 = False
        str_name = "self.Chap0{0}.isChecked()"

        for i in range(0, 8):
            if eval(str_name.format(i)) == 1:
                judge2 = True

        if judge2:
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = ChoiceType()
    c.show()
    sys.exit(app.exec_())