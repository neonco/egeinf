s = open('24.txt').readline()

alph = set(s)
print(alph)
# поменяю все буквы на пробел для удобства сплита
for bukva in alph:
    if bukva.isalpha():
        s = s.replace(bukva, ' ')
# print(s)

# разбиваем по пробелам
s = s.split()
# переводим в числа для сортировки и избавления от нулей слева
s = [int(x) for x in s]
# отсортируем и найдём среди последних чётное
s = sorted(s)
# ответ 39168781038
print(s)