# import re

# import datetime as dt
users = {
    'user': {
        'birthday': '20000202',
        'password': 'a',
        'role': 'viewer'
    },
    'test': {
        'password': 'bbb',
        'birthday': '20250506',
        'role': 'admin'
    }
}

def showTable():
    for i in users:
        print(f"아이디: {i}")
        print_user_data(i)

current_user_id = ""
current_user_role = ""

def idChk(id):
    if id in users:
        return False
    return True

# def pwdChk(pwd):
#     if len(pwd) < 8:
#         return False
#     special_chars = r'@$!%*#?&'
#     vregex = re.compile(f'^(?=.*[A-Za-z])(?=.*\d)(?=.*[{re.escape(special_chars)}])[A-Za-z\d{re.escape(special_chars)}]{{10,}}$')
#     return vregex.match(pwd)

def pwdChk2(pwd):
    if len(pwd) < 8:
        return False
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
    special_flag = False
    number_flag = False
    for i in pwd:
        if i.isdigit():
            number_flag = True
        if i in special_chars:
            special_flag = True

    return special_flag and number_flag

def dayCheck(days):
    [year, month, day] = [int(days[0:4]), int(days[4:6]), int(days[6:])]
    if month > 13 or day > 31 or day < 0 or month < 0:
        return False
    return True

def login():
    global current_user_id
    global current_user_role
    if current_user_id != "":
        print("로그아웃 되었습니다")
        current_user_id = ""
        current_user_role = ""
        return
    id = input("아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")

    if id in users:
        if users[id]["password"] == password:
            current_user_id = id
            current_user_role = users[id]["role"]
            print(current_user_id, current_user_role)
            print("로그인 성공!")
        else:
            print("로그인 실패(비밀번호)")
    else:
        print("로그인 실패(아이디)")

def registerInput():
    id= None
    password = None
    birthday = None
    role = None
    id = input("아이디를 입력하세요: ")
    if idChk(id):    
        password = input("비밀번호를 입력하세요: ")
        if pwdChk2(password):
            birthday = input("생년월일을 입력하세요(YYYYMMDD)")
            if dayCheck(birthday):
                role = input("역할을 입력하세요(admin, viewer, editor): ")
            else:
                print("생년월일 양식이 잘못되었습니다")
        else:
            print("비밀번호 양식이 잘못되었습니다")
    else:
        print("id 양식이 잘못되었습니다")
    return [id, password, birthday, role]

def register():
    while True:
        [id, password, birthday, role] = registerInput()
        if id != None and password != None and birthday != None and role != None:
            users[id] = {"password": password, "birthday": birthday, "role": role}
            showTable()
            print("등록되었습니다")
            break

def kick(role):
    global current_user_id
    global current_user_role
    if role == "admin":
        print(f"현재 유저들: {*users.keys(),}")
        print(f"삭제할 아이디를 입력하세요 {current_user_id} 관리자님")
        id = input("삭제할 아이디: ")
        if id in users:
            del users[id]
            showTable()
            if(id == current_user_id):
                current_user_id = ""
                current_user_role = ""
            print("정상적으로 삭제되었습니다")
        else:
            print("해당 아이디가 존재하지 않습니다")
    else:
        # 탈퇴
        yn = input("정말로 탈퇴하시겠습니까? Y/N")
        if yn == 'Y':
            del users[current_user_id]
            current_user_id = ""
            current_user_role = ""
            showTable()
            print("정상적으로 탈퇴되었습니다")
        else:
            print("탈퇴되었습니다")

def modify():
    global current_user_id
    global current_user_role
    print(f"현재 {current_user_id} 님의 정보입니다.\n")
    print_user_data(current_user_id)
    
    password = input("새 비밀번호: ")
    birthday = input("새 생일(YYYYMMDD): ")
    role = input("새 역할: ")

    users[current_user_id]["password"] = password
    users[current_user_id]["birthday"] = birthday
    users[current_user_id]["role"] = role
    current_user_role = role
    print("성공적으로 수정되었습니다.")
    showTable()

    return
def modifiyAdmin():
    while True:
        id = input("수정할 유저의 아이디: ")
        if idChk(id) == False:
            break
        else:
            print("없는 아이디입니다. 다시 입력하세요")
    password = input("새 비밀번호: ")
    birthday = input("새 생일(YYYYMMDD): ")
    role = input("새 역할: ")
    users[id]["password"] = password
    users[id]["birthday"] = birthday
    users[id]["role"] = role
    print("수정되었습니다")
    showTable()

    return

def print_user_data(user_id):
    translate = {
        'birthday': '생일',
        'password': '비밀번호',
        'role': '역할'
    }
    for key, value in users[user_id].items():
        print(f"{translate[key]}: {value}")
        
    print("=====================")
    
def menu():
    global current_user_role
    global current_user_id
    while True:
        if current_user_id != "":
            print(f"반갑습니다 {current_user_id} 님")
        menu = input(f"메뉴를 선택하세요\n {"로그인(0)" if current_user_id == "" else "로그아웃(0)"}, 회원가입(1), 탈퇴(2) {", 수정(3)" if current_user_id != "" else ""}\n")
        match menu:
            case "0":
                login()
            case "1":
                register()
            case "Test":
                print(users)
            case "2":
                print(current_user_id, current_user_role)
                if current_user_role == "":
                    print("먼저 로그인해주세요")
                else:
                    kick(current_user_role)
            case "3":
                if current_user_role != "viewer":
                    modifiyAdmin()
                else:
                    modify()
            case _:
                print("잘못된 입력입니다")
        
menu()