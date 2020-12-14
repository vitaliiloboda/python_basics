proceeds = int(input('Введите значение выручка: '))
costs = int(input('Введите значение издержек: '))
profit = proceeds - costs

if proceeds > costs:
    print('Фирма работает с прибылью')
    print(f'Рентабельность выручки: {profit / proceeds * 100:.2f}%')
    number_employees = int(input('Введите чисельность сотрудников фирмы: '))
    print(f'Прибыль фирмы на одного сотрудника: {profit / number_employees:.2f}')

elif proceeds == costs:
    print('Фирама работает в ноль')
else:
    print('Фирама работает с убытком')
