import os

def find_bank(bank_name):
    path = os.getcwd()
    dir_list = os.listdir(path)
    for bank_dir in dir_list:
        if bank_dir.find(bank_name) != -1:  # -1代表文件夹名称中没有bank_name
            bank_path = path + "/" + bank_dir
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