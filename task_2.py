from random import randint

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list2 = [randint(0, 20) for i in range(20)]

new_list = [my_list[i + 1] for i in range(0, len(my_list) - 2) if my_list[i + 1] > my_list[i]]
print(f'Исходный список: {my_list}')
print(f'Результат: {new_list}')

new_list2 = [my_list2[i + 1] for i in range(0, len(my_list2) - 2) if my_list2[i + 1] > my_list2[i]]
print(f'Исходный список: {my_list2}')
print(f'Результат: {new_list2}')

