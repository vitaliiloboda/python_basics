goods_n = int(input('Сколько товаров вы хотите ввести: '))
n = 0
goods_list = []

for i in range(goods_n):
    n += 1
    name = input('Введите название товара: ')
    price = input('Введите цену товара: ')
    number = input('Введите количество товара: ')
    unit = input('Введите единицу измерения товара: ')

    specification = {'название': name, 'цена': price, 'количество': number, 'ед': unit}
    product = (n, specification)
    goods_list.append(product)

print(goods_list)

keys = list(goods_list[0][1].keys())
my_dict = {}

for k in keys:
    values = []
    for i in goods_list:
        values.append(i[1].get(k))
    my_dict.update({k: values})
print(my_dict)
