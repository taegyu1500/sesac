import datetime as dt
currentList = {
        "20250827": [
            {
            "title": "",
            "content": "",
            "order": 0,
            }
        ]
    }

    
def inputting():
    input1 = input("제목: ")
    input2 = input("내용: ")
    return [input1, input2]

def diaryFormat(dict):
    print(f"\n제목:{dict["title"]}\n내용:{dict["content"]}\n")

def today():
    today = dt.datetime.now()
    return [today.year, today.strftime("%m"), today.strftime("%d")]

def menuChoicing():
    # print(currentList)
    menu = input("일기 쓰기(0), 일기 확인(1), 일기 삭제(2), 일기 수정(3): \n")
    match menu:
        case "0":
            writing()
        case "1":
            reading()
        case "2":
            deleting()
        case "3":
            modifing()
        case _:
            print("잘못된 입력입니다")

def writing():
    [title, content] = inputting()
    RawDate = today()
    date = str(RawDate[0])+str(RawDate[1])+str(RawDate[2])
    if date not in currentList: 
        currentList[date] = []
    currentList[date].append({"title": title, "content": content, "order": len(currentList[date])})

def reading():
    date = input("날짜를 입력해주세요(YYYYMMDD): ")
    if date in currentList:
        if len(currentList[date]) > 1:
            order = int(input("보고싶은 일기 번호: "))
            diaryFormat(currentList[date][order])
        else:
            diaryFormat(currentList[date][0])
    else:
        print("해당 날짜에 일기를 찾지 못했습니다")

def deleting():
    date = input("날짜를 입력해주세요(YYYYMMDD): ")
    if date in currentList:
        if len(currentList[date]) > 1:
            order = int(input("삭제하려는 일기 번호: "))
            currentList[date].remove(currentList[date][order])
        else:
            currentList.remove(currentList[date])
        print("삭제가 완료되었습니다")
    else:
        print("해당 날짜에는 일기가 없습니다")

def modifing():
    date = input("날짜를 입력해주세요(YYYYMMDD): ")
    if date in currentList:
        if len(currentList[date]) > 1:
            order = int(input("수정하려는 일기 번호: "))
            if currentList[date][order]:
                [title, content] = inputting()
                currentList[date][order]["title"] = title
                currentList[date][order]["content"] = content
        else:
            [title, content] = inputting()
            currentList[date][0]["title"] = title
            currentList[date][0]["content"] = content
        print("수정이 완료되었습니다")
    else:
        print("해당 날짜에는 일기가 없습니다")

while True:
    menuChoicing()