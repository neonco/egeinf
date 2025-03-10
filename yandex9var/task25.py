from fnmatch import fnmatch

mask = "17*023?9"
for n in range(1_800_000_000, 5, -1):
    if fnmatch(str(n), mask):
        sum_digit = sum(int(x) for x in str(n))
        if sum_digit % 11 == 0:
            print(n, sum_digit // 11)

# осторожнее! в ответ надо записать первых пять строк, но снизу вверх!