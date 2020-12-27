f_name = open('text_1.txt', 'w', encoding='utf-8')

while True:
    text = input('Пустая строка завершает ввод. Введите строку: ')
    if text == '':
        break
    print(text, file=f_name)

f_name.close()
