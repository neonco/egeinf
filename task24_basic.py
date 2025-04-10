# 19717
with open('24.5_19717.txt') as file: # прочитал файл
    s = file.readline()
# важные проверки
print(len(s)) # длина строки
print(set(s)) # все символы используемые в строке
# надо найти максимальную по длине подстроку в которой
# буква M встречается не более 278 раз

# делаю алгоритм на руках из куска строки
# буду искать М не более 3 раз
# AIAELAALMAIGELLGLMMLGLELLEGGMMRE
# ['AIAELAAL', 'AIGELLGL', '', 'LGLELLEGG', '', 'RE'] сплит по М
# [8, 8, 0, 9, 0, 2] замена слов на их длину
# берём по 4 и не забываем добавить 3 пропущенные М

s = s.split('M')
s = [len(x) for x in s]
# внутри должно быть 278 М, тогда их покрывают поверх 279 отрезков
res = []
for i in range(len(s)):
    r = sum(s[i:i+279]) + 278 # не теряем наши M
    res.append(r)

print(max(res))


