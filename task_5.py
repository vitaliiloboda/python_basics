def my_func():
    result = 0

    while True:
        num_str = input('Введите строку числа разделенные пробелами. Чтобы завершить программу введите "q": ')
        numbers_str = num_str.split()

        if 'q' in numbers_str:
            numbers = list(map(int, numbers_str[:-1]))
            result = result + sum(numbers)
            print(f'Промежуточная сумма: {sum(numbers)}, Итоговая сумма: {result}')
            print('Программа заверщина!')
            break
        else:
            numbers = list(map(int, numbers_str))
            result = result + sum(numbers)
            print(f'Промежуточная сумма: {sum(numbers)}, Итоговая сумма: {result}')


my_func()
