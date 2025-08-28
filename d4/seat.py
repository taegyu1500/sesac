reservation = [[True for _ in range(5)] for _ in range(5)]
def showSeat():
    showing = []
    for i in reservation:
        row = []
        for j in i:
            if j:
                row.append("ㅇ")
            else:
                row.append("X")
        showing.append(row)
    for i in showing:
        print(i)

def recommand(row, col):
    answer = [False]*4
    # 우, 하, 좌, 상
    if row+1 < 5 and reservation[row+1][col]:
        answer[0] = True
    if col+1 < 5 and reservation[row][col+1]:
        answer[1] = True
    if reservation[row-1][col] and row-1 >= 0:
        answer[2] = True
    if reservation[row][col-1] and col-1 >= 0:
        answer[3] = True
    return answer

while True:
    showSeat()
    while True:
        try:
            row = int(input("Select row: ") or 0) -1
            break
        except:
            print("잘못된 입력입니다. 다시 입력하세요")
    while True:
        try:
            col = int(input("Select col: ") or 0) -1
            break
        except:
            print("잘못된 입력입니다. 다시 입력하세요")
    # row = int(input("Select row: ") or 0) -1
    # col = int(input("select col: ") or 0) -1

    if 0 <= row < 5 and 0 <= col < 5:
        if reservation[row][col]:
            reservation[row][col] = False
            print(f"자리({row+1}-{col+1})번 예약에 성공했습니다")
        else:
            print(f"자리({row+1}-{col+1})번은 이미 예약되었습니다")
            vacant = recommand(row, col)
            # print(vacant)
            if True not in vacant:
                print(f"자리({row+1}-{col+1})주변 예약 가능 자리가 없습니다")
                continue
            for i in range(0, len(vacant)):
                if vacant[i]:
                    match(i):
                        case 0:
                            print(f"주변 자리({row+2}-{col+1})는 예약 가능한 상태입니다.")
                        case 1:
                            print(f"주변 자리({row+1}-{col+2})는 예약 가능한 상태입니다.")
                        case 2:
                            print(f"주변 자리({row}-{col+1})는 예약 가능한 상태입니다.")
                        case 3:
                            print(f"주변 자리({row+1}-{col})는 예약 가능한 상태입니다.")
    else:
        print("예약 가능한 범위를 벗어난 입력입니다")
        break
        
