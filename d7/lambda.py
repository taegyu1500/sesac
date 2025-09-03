from random import randint
from functools import reduce, partial
a = lambda b,c: b+c
print(a(2,3))

l = [randint(5,1000) for _ in range(5)]

s = map(lambda x: x**2, l)
print(l, list(s))

t = sorted(l, key=lambda x:x%2==0)
print(t)

r = reduce(lambda a,b: a+b, l)
print(r)

square = partial(pow, exp=2)
print(square(5))