from itertools import count, cycle

for el in count(int(input('Введите начальное число: '))):
    if el > 20:
        break
    else:
        print(el)

print('-' * 50)

c = 0
for el in cycle('qwertyuiop'):
    if c > 15:
        break
    else:
        print(el)
    c += 1
