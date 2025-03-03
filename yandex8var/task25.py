def allah(n):
    res = []
    for d in range(1, int(n**0.5)+1):
        if n % d == 0:
            res.append(d)
            res.append(n//d)
    return sorted(set(res))


for n in range(800_001, 800_001+100):
    sr = allah(n)[:-1]
    sr = [x for x in sr if x%100 == 14 and x != 14]
    if sr:
        print(n, allah(n))
