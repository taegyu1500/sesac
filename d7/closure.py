# def make_counter(count_from):
#     cnt = count_from
#     def counter():
#         nonlocal cnt
#         cnt +=1
#         return cnt
#     return counter

# c = make_counter(0)
# print(c())
# print(c())

def login_attempt():
    count = 0
    def login_fail():
        nonlocal count
        count += 1
        return count
    
    def login_success():
        nonlocal count
        count = 0
        return count
    
    def login(result):
        nonlocal count
        if(result and count < 3):
            login_success()
            return "로그인 성공, 실패회수 초기화"
        elif count < 3:
            login_fail()
            return f"로그인 실패, {count}회 실패함"
        else:
            return "계정 잠김"
    
    return login

a = login_attempt()            
b = login_attempt()
print(a(False), 'a')
print(b(False), 'b')
print(a(False), 'a')
print(a(True), 'a')
print(a(False), 'a')
print(a(False), 'a')
print(a(False), 'a')
print(a(True), 'a')
print(b(False), 'b')
print(b(True), 'b')

def add(a:int, b:int) -> int:
    return a+b

print(add("가", "나"))
    