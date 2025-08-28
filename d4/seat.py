reservation = [[True]*3]*3
print(reservation)

row = int(input("Select row(0-2): "))
col = int(input("select col(0-2): "))

if 0 <= row < 3 and 0 <= col < 3:
    if reservation[row][col]:
        reservation[row][col] = False
        print(f"자리({row+1}-{col+1})번 예약에 성공했습니다")
    else:
        print(f"자리({row+1}-{col+1})번은 이미 예약되었습니다")
else:
    print("잘못된 입력입니다")

