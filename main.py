n, k = [int(el) for el in input().split()]
data = []
for _ in range(n):
    l, *recipe = [int(el) for el in input().split()]
    data.append((l, set(recipe)))

data = sorted(data)[::-1]
data = [r for l, r in data]

cl = 1
clus = [0]*len(data)

for i in range(len(data)):
    if clus[i] == 0:
        clus[i] = cl
        t = data[i]
        for j in range(i+1, len(data)):
            if data[j].issubset(t):
                clus[j] = cl
                t = data[j]
        cl += 1
if 0 in clus:
    print(0)
print(len(set(clus)))