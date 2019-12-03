import json
from choice_function import *

def get_data(index):
    with open('questions.json', 'r', encoding='utf-8') as f:
        file_data = json.load(f)
        data_list = []
        num = len(index)
        for key, _ in file_data.items():
            if key[:num].find(index) == 0:
                data = file_data[key]
                data.append(key)
                data_list.append(data)
        return data_list[1:]

def read():
    with open('questions.json', 'r', encoding='utf-8') as f:
        file_data = json.load(f)
    return list(file_data.keys())[0][0]

def distribute_question(d_chap, d_type):
    d_questions = list()
    for i in d_type:
        for j in d_chap:
            d_index = read() + i + j.rjust(2, '0')
            d_questions.extend(get_data(d_index))
    print(d_questions)
    return d_questions
