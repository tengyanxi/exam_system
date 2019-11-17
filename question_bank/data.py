from read_data import read_data

def get_data(bank_name, type_, chapters):
    data_list = read_data(bank_name, type_, chapters)
    return data_list


if __name__ == "__main__":
    data_list = get_data("马克思", "多选", ["绪论"])
    print(data_list)