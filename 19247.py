pairs = []
for x in range(1, 1000):
    for y in range(1, 1000):
        pairs.append([x, y])

for a in range(0, 1001):
    for x, y in pairs:
        f = (x - 3*y < a) or (y > 400) or (x > 56)
        if f == 0:
            break
    else:
        print(a)

