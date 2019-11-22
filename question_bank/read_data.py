import xlrd
from get_path import find_bank, find_question

def read_data(bank_name, type_, chapters):
    bank_path = find_bank(bank_name)
    questions_path = find_question(bank_path, type_, chapters)
    data_list = []
    for question_path in questions_path:
        data_list = read_bank(question_path)
    return data_list

def read_bank(question_path):
    data_list = []
    workbook = xlrd.open_workbook(question_path)
    sheet = workbook.sheets()[0]
    nrows = sheet.nrows
    for i in range(nrows):
        values = sheet.row_values(i)
        values_wash = []
        for value in values:
            move = dict.fromkeys((ord(c) for c in u"\xa0\n\t"))
            value_wash = str(value).translate(move)
            values_wash.append(value_wash)
        data_list.append(values_wash)
    return data_list