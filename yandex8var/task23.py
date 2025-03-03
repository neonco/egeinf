def f(x, end):
    if x == end:
        return 1
    if x > end:
        return 0
    m = [
        f(x+3, end),
        f(x*2, end),
        f(x*x, end),
         ]
    return sum(m)

print(f(2, 128))
# в условии либо есть 12, либо нет 20
# могут быть траектории, которые подходят под оба условия
# нельзя просто взять общее число и вычесть сначала первый вариант, потом второй
# будем собирать все траектории по числам

tr = []

def g(x, end, track=[]):
    if x == end:
        return tr.append(track)
    if x > end:
        return 0
    m = [
        g(x+3, end, track + [x]),
        g(x*2, end, track + [x]),
        g(x*x, end, track + [x]),
         ]
    return any(m)

g(2, 128)
print(len(tr))
tr = [t for t in tr if (12 in t) or (20 not in t)]
print(len(tr))
