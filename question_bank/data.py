from judge import judgement_questions

def get_data(bank_name, type_, chapters):
    if type_ == "判断":
        data_dic = judgement_questions(bank_name, type_, chapters)
    return data_dic


if __name__ == "__main__":
    data = get_data("马克思", "判断", ["绪论"])
    print(data)