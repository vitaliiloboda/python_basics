my_str = input('Введите строку из нескольких слов через пробел: ')
my_list = my_str.split(' ')

for k, i in enumerate(my_list, 1):
    print(k, i[:10])
