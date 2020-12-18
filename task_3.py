month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

if month in winter:
    print(f'{month}-й месяц это зима')
elif month in spring:
    print(f'{month}-й месяц это весна')
elif month in summer:
    print(f'{month}-й месяц это лето')
elif month in autumn:
    print(f'{month}-й месяц это осень')

year = {12: 'зима', 1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна',
        5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'зима', 11: 'зима', }

print(f'{month}-й месяц это {year[month]}')
