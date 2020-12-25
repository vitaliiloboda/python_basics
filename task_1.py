from sys import argv

try:
    script_name, hours, rate, bonus = argv
    salary = (int(hours) * int(rate)) + int(bonus)
    print(f'Зарплата равана: {salary}')
except ValueError:
    print('Введите параметры корректно')

