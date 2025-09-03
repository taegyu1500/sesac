import random

def add_three_numbers(a,b,c):
    return a + b + c

l = [[random.randint(1,100) for _ in range(3)] for _ in range(3)]

def array_add(list):
    return [sum(x) for x in zip(*list)]
print(l, *l, array_add(l))
# print(add_three_numbers(*l))
# print(*l)

def add_two_numbers(first, second):
    return first + second

d = {"first": 1, "second": 2}


s = [[[random.randint(1,100) for _ in range(3)] for _ in range(3)] for _ in range(3)]
print(s, *s,)
# *d -> key, **d -> value
print(add_two_numbers(*d))