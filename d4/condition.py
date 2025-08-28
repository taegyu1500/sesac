# age = int(input("나이 입력: "))
# discount_rate= 0

# if age <= 5 or age >= 65:
#     discount_rate = 10
#     print(f"{"유아" if age <= 5 else "노인"} 할인 {discount_rate}%")

# temp = int(input("온도: "))

# if temp < -20:
#     print("very cold")
# elif temp < -0 :
#     print("cold")
# elif temp >= 0 and temp < 20:
#     print("temperature") 
# elif temp >= 20:
#     print("hot")

countries = {
    "Korea": {
        "lan": "Korean", "greeting": "안녕"
    },
    "Japan": {
        "lan": "Japanase", "greeting": "Japan hello"
    },
}

user_input = input("Country: ")
if user_input in countries:
    for key, value in countries[user_input].items():
        print(f"{key}: {value}")
else:
    print("없습니다")

if user_input == "Korea":
    print(f"language: {countries[user_input]["lan"]}\ngreetings: {countries[user_input]["greeting"]}")
elif user_input == "Japan":
    print(f"language: {countries[user_input]["lan"]}\ngreetings: {countries[user_input]["greeting"]}")
else:
    print("없습니다")