from math import dist
from collections import Counter

f = open('27A_18677.txt').readlines()
f = [x.replace(',', '.').split() for x in f]
f = [(float(x), float(y)) for x, y in f]

print(len(f))
cl = [10**10]*len(f)

for i, p in enumerate(f):
    cl[i] = min(cl[i], i)
    for j, q in enumerate(f):
        if dist(p, q) <= 1:
            cl[i] = cl[j] = min(cl[i], cl[j])

c = Counter(cl)
print(c)
cl1 = [x for i, x in zip(cl, f) if i == 11]
print(cl1)

