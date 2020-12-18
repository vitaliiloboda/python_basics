list_str = input('Введите элементы списка через пробел: ')
my_list = list_str.split()

list_len = len(my_list)
i = 0

while i < list_len - 1:
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i += 2

print(my_list)
