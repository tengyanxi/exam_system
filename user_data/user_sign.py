import json

def sign_in(user_name, password):
    with open('user_data.json', 'r') as f:
        data_dic = json.load(f)
    try:
        if data_dic[user_name] == password:
            return True
        elif data_dic[user_name] != password:
            return "pw_false"
    except KeyError:
        return "name_false"

def sign_up(user_name, password):
    with open('user_data.json', 'r', encoding='UTF-8') as f:
        data_dic = json.load(f)
        try:
            bo_name = bool(data_dic[user_name])
        except KeyError:
            bo_name = False
        if bo_name:
            return False
    with open('user_data.json', 'w', encoding='UTF-8') as f:
            data_dic[user_name] = password
            json.dump(data_dic, f, ensure_ascii=False)


if __name__ == "__main__":
    sign_up("sb", "123")
    sign_in("sb", "123")