number = int(input('Введите целое положительное число: '))

k = 1
a = None
max_number = 0

while True:
    a = number % 10 ** k // 10 ** (k - 1)

    if max_number < a:
        max_number = a

    if (number % 10 ** k) == number:
        break

    k += 1

print(f'Самая большая цифра в числе: {max_number}')
