pairs = []
for start in range(-100, 400):
    for end in range(start + 1, 400):
        pairs.append([start, end])

p = range(10, 150+1)
q = range(160, 250+1)
r = range(240, 300+1)

res = 1221221121221
for start, end in pairs:
    a = range(start, end+1)
    for x in range(-100, 400):
        f = (not (x in q) or (x in p)) or ((x in a) or (x in r))
        if not f:
            break
    else:
        res = min(end - start, res)
print(res)

