from functools import lru_cache

@lru_cache()
def f(n):
    if n == 1:
        return 2
    elif n > 1 and f(n-1) < 7555444:
        return f(n-1) + 6
    else:
        return f(n-1) - 7555444


res = []
for n in range(1, 7555444+1000):
    res.append(f(n))

print(max(res))