class OnlyNumbersErr(Exception):
    def __init__(self, txt):
        self.txt = txt


numbers = []

while True:
    try:
        number = input('Введите число:')

        if number == 'stop':
            break

        if not number.isdigit():
            raise OnlyNumbersErr('Вы ввели не число')

    except OnlyNumbersErr as err:
        print(err)

    else:
        numbers.append(int(number))

print(numbers)
