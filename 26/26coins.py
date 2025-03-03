m = [1, 2, 3, 10, 12, 15, 15]

res = [1]+[0]*(sum(m))
for coin in m:
    temp = res[::]
    for i in range(coin, len(res)):
        res[i] = res[i] + temp[i-coin]
    print(res)
