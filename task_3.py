def my_func(num1, num2, num3):
    """Возвращает сумму наибольших двух аргументов"""
    num_list = [num1, num2, num3]
    """Создание списка из введенных аргументов: num1, num2, num3"""
    num_list.sort(reverse=True)
    """Сортировка списка по возрастанию"""
    return num_list[0] + num_list[1]


print(my_func(2, 9, 3))
