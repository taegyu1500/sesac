while True:
    try:
        num = int(input("숫자 입력: "))
        break
    except:
        print("잘못된 입력입니다")
print(f"{"짝수" if num%2==0 else "홀수"}")

user_input = input("알파벳 입력: ")
n_list = ['a', 'b', 'c']
print(f"{"Yes" if user_input in n_list else "No"}")

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekends = ["Saturday", "Sunday"]

day = input("Enter a day of the week: ")

print(f"{day} is {"weekdays" if day in weekdays else "weekends" if day in weekends else "wrong"}")