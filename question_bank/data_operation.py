import json

def judge_in(name):
    with open("name_pwd.json", "r") as f:
        nameData = json.load(f)
    if name in nameData :
        return True
    else:
        return False

def judge_match(name, pwd):
    with open("name_pwd.json", "r") as f:
        nameData = json.load(f)
    if nameData[name] == pwd:
        return True
    else:
        return False

def write_data(name, pwd):
    with open("name_pwd.json", "r") as f1:
        nameData = json.load(f1)
    with open("name_pwd.json", "w") as f2:
        nameData[name] = pwd
        json_data = json.dumps(nameData)
        f2.write(json_data)
        f2.close()
