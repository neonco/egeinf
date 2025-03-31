a = 'SIRIUS'
b = 'LYCEUM'

# print(ord('A'))
# print(ord('Z'))

x = [ord(el)-55 for el in a]
y = [ord(el)-55 for el in b]
print(x, y)

def base_to_dec(n, base):
    return sum([razryad * base**i for i, razryad in enumerate(n[::-1])])

for p in range(max(x)+1, 1000):
    for q in range(max(y)+1, 1000):
        a, b = base_to_dec(x, p), base_to_dec(y, q)
        if (a + b) % 2025 == 0:
            print(p, q, (a + b)//2025)

# p = 40, q = 35, otvet 2009655