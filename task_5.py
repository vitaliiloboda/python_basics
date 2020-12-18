new_number = None
my_list = [7, 5, 3, 3, 2]

while True:
    new_number_str = input('Введите новый элемент рейтинга или чтобы завершить программу введите "end": ')
    if new_number_str == 'end':
        break

    new_number = int(new_number_str)

    for i in range(len(my_list)):
        if new_number >= my_list[i]:
            count = my_list.count(new_number)
            my_list.insert(my_list.index(my_list[i]) + count, new_number)
            break
        elif new_number not in my_list and new_number <= my_list[len(my_list) - 1]:
            my_list.append(new_number)

    print(f'Пользователь ввел число {new_number}. Результат: {my_list}')
