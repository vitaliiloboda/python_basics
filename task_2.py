time = int(input('Введите время в секундах: '))

print(f'{time // 3600:02d}:{time % 3600 // 60:02d}:{time % 3600 % 60:02d}')
