def f(x, end):
    if x == end:
        return 1
    if x < end:
        return 0
    if x % 3 == 0:
        return f(x-5, end) + f(x//3, end)
    else:
        return f(x-5, end) + f(x - x%3, end)
    
print(f(103, 73) * f(73, 24))