movies = {
    "Action": [
        "John Wick", "Matrix"
    ],
    "Romance": [
        "asdf"
    ],
    "Horror": [
        "Horror1", "Horror2"
    ],
    "Kid": [
        "Kid1", "Kid2",
    ]
}
user_input = input("장르 선정(Action, Romance, Horror, Kid): ")

if(user_input in movies):
    for i in movies[user_input]:
        print(i)
else:
    print("장르가 없습니다")

