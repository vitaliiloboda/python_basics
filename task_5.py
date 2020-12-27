from random import randint

numbers_list = [str(randint(0, 100)) for i in range(15)]
numbers_str = ' '.join(numbers_list)

with open('text_5.txt', 'w+', encoding='utf-8') as f:
    f.write(numbers_str)
    f.seek(0)
    content = f.read()

    numbers_str = content.split()
    numbers = list(map(int, numbers_str))
    print(f'Сумма чисел: {sum(numbers)}')
