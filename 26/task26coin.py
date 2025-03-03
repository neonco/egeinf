from functools import cache

with open('26_2653.txt') as file:
    data = file.readlines()[1:]

data = [int(x) for x in data]
print(len(data), len(set(data)))

data = [12, 13, 14, 100, 4, 3, 2]

@cache
def f(start, end, m):
    if start == end:
        return 1
    if start > end:
        return 0
    for coin in m:
        coins = m.copy()
        if len(coins) == 0:
            return 0
        else:
            coins.remove(coin)
            if f(start + coin, end, coins) == 1:
                return 1

for i in range(1, sum(data)+1):
    print(i, f(0, i, data))
# меняли, надо доделать


