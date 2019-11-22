import os
import json
from read_data import read_bank

def find_bank():
    path_ = os.getcwd()
    dir_list = os.listdir(path_)
    for bank_dir in dir_list:
        full_bank_path = os.path.join(path_, bank_dir)
        if os.path.isdir(full_bank_path):
            bank_key = judge_dir(bank_dir)
            if bank_key != False:
                file_list = os.listdir(full_bank_path)
                for file in file_list:
                    file_path = full_bank_path + "/" + file
                    data_key = bank_key + judge_file(file)
                    data_list = read_bank(file_path)
                    data_dic = {}
                    for i in range(len(data_list)):
                        data_dic[data_key + str(i).zfill(4)] = data_list[i]
                    data_add(data_dic)

def judge_dir(bank_dir):
    if bank_dir.find("马克思") != -1:
        return "0"
    if bank_dir.find("近代史") != -1:
        return "1"
    if bank_dir.find("思修") != -1:
        return "2"
    return False

def judge_file(file):
    index = ""
    if file.find("判断") != -1:
        index += "0"
    if file.find("单选") != -1:
        index += "1"
    if file.find("多选") != -1:
        index += "2"
    
    if file.find("绪论") != -1:
        index += "00"
    if file.find("第一") != -1:
        index += "01"
    if file.find("第二") != -1:
        index += "02"
    if file.find("第三") != -1:
        index += "03"
    if file.find("第四") != -1:
        index += "04"
    if file.find("第五") != -1:
        index += "05"
    if file.find("第六") != -1:
        index += "06"
    if file.find("第七") != -1:
        index += "07"

    return index

def data_add(dic):
    with open('data.json', 'a', encoding='utf-8') as f:
        json.dump(dic, f, ensure_ascii=False, indent = 4)

find_bank()