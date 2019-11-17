import os
import xlrd

def find_bank(bank_name):
    path = os.getcwd()
    print(path)
    dir_list = os.listdir(path)
    print(dir_list)
    print(bank_name)
    for bank_dir in dir_list:
        if bank_dir.find(bank_name) != -1:  # -1代表文件夹名称中没有bank_name
            bank_path = path + "/" + bank_dir
            print(bank_path)
            return bank_path

def find_question(bank_path, type_, chapters):
    file_list = os.listdir(bank_path)
    whole_question_list = []
    for file in file_list:
        if file.find(type_) != -1:
            file_path = bank_path + "/" + file
            whole_question_list.append(file_path)
    question_list = []
    for file in whole_question_list:
        for chapter in chapters:
            if file.find(chapter) != -1:
                question_list.append(file)
                break
    return question_list

def get_data(bank_name, type_, chapters):
    if type_ == "判断":
        data = judgement_questions(bank_name, type_, chapters)
    return data

def judgement_questions(bank_name, type_, chapters):
    bank_path = find_bank(bank_name)
    question_path = find_question(bank_path, type_, chapters)
    return question_path


if __name__ == "__main__":
    data = get_data( "马克思", "判断", ["第一章"])
    print(data)
    print(1)