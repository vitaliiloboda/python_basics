class ZeroErr(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = int(input('Введите делимое число: '))
    b = int(input('Введите делитель: '))

    if b == 0:
        raise ZeroErr('На ноль делить нельзя')

except ZeroErr as err:
    print(err)

except ValueError:
    print('Необходимо ввести число. Попробуйте еще раз.')

else:
    print(a / b)
