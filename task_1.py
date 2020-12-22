def division(num1, num2):
    return num1 / num2


num1 = int(input('Ввелидет делимое число: '))
num2 = int(input('Ввелидет делитель число: '))

try:
    print(division(num1, num2))
except ZeroDivisionError:
    print('На ноль делить нельзя')
