import json

def get_data(index):
    """
    输入数据的ID的任意前N位
    以list形式返回符合该ID的任意前N位的所有数据
    """
    with open('exam_bank.json', 'r', encoding='utf-8') as f:
        file_data = json.load(f)
        data_list = []
        num = len(index)
        for key, _ in file_data.items():
            if key[:num].find(index) != -1:
                data = file_data[key]
                data.append(key)
                data_list.append(data)
        return data_list


if __name__ == "__main__":
    print(len(get_data('01')))
