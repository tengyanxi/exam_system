import xlrd
from get_path import find_bank, find_question

def judgement_questions(bank_name, type_, chapters):
    bank_path = find_bank(bank_name)
    questions_path = find_question(bank_path, type_, chapters)
    data_dic = get_judgement_data(questions_path)
    return data_dic

def get_judgement_data(questions_path):
    data_list = []
    for question_path in questions_path:
        data_list = read_judge_bank(data_list, question_path)
    return data_list


def read_judge_bank(data_list, question_path):
    workbook = xlrd.open_workbook(question_path)
    sheet = workbook.sheets()[0]
    nrows = sheet.nrows
    for i in range(nrows):
        data_list.append(sheet.row_values(i))
    return data_list