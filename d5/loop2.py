import random

score = []
num = 20
for i in range(num):
    score.append(random.randint(0,100))
# max_score = score[0]
# for i in score:
#     if i > max_score:
#         print(f"max updated! {max_score} -> {i}")
#         max_score = i
#     else:
#         print(f"max stays! {i}, max:{max_score} ")

# print(max(score))
# print(max_score, score)
avg_score = 0
for i in score:
    avg_score += i
print(avg_score/num)

loop = 0
avg = 0
while avg != 50:
    loop += 1
    score = []
    for i in range(num):
        score.append(random.randint(0,100))
    avg_score = 0
    for i in score:
        avg_score += i
    avg = avg_score/num

dict = {}
for i in range(num):
    dict[i] = random.randint(0, i)

for key,value in dict.items():
    print(f"{key}:{value}")