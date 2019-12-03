import json
from ChoiceType import *

def get_data(index):
    with open('data.json', 'r', encoding='utf-8') as f:
        file_data = json.load(f)
        data_list = []
        num = len(index)
        for key, _ in file_data.items():
            if key[:num].find(index) == 0:
                data = file_data[key]
                data.append(key)
                data_list.append(data)
        return data_list[1:]

def distribute_question(d_sub, d_chap, d_type):
    d_questions = list()
    for i in d_type:
        for j in d_chap:
            d_index = d_sub + i + j.rjust(2, '0')
            d_questions.extend(get_data(d_index))
    return d_questions