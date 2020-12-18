my_list = [125, 'hello', True, 3.45, [1, 2], b'text', (78, 234), {5, 6}, None, {'a': 1, 'b': 2}]

for k, i in enumerate(my_list, 1):
    print(f'{k} Значение: {i}, Тип данных: {type(i)}')
