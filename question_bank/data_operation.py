import json

def open_json():
    try:
        with open("name_pwd.json", "r") as f:
            nameData = json.load(f)
    except:
        nameData = {}
    return nameData

def judge_in(name):
    nameData = open_json()
    if name in nameData :
        return True
    else:
        return False

def judge_match(name, pwd):
    nameData = open_json()
    if nameData[name] == pwd:
        return True
    else:
        return False

def write_data(name, pwd):
    nameData = open_json()
    with open("name_pwd.json", "w") as f2:
        nameData[name] = pwd
        json_data = json.dumps(nameData)
        f2.write(json_data)
        f2.close()
