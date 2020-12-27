numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_text = []

with open('text_4.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()

    for line in content:
        for item in numbers:
            if item in line:
                new_line = line.replace(item, numbers.get(item))
                new_text.append(new_line)

with open('new_text_4.txt', 'w', encoding='utf-8') as new_f:
    new_f.writelines(new_text)

# ****************************************вариант_2*********************************************************


numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_text = []

with open('text_4.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    print(content)
    for line in content:
        words = line.split()
        new_word = numbers[words[0]]
        words.pop(0)
        words.insert(0, new_word)
        s = ' '.join(words)
        new_text.append(f'{s}\n')

with open('new_text_4.txt', 'w', encoding='utf-8') as new_f:
    new_f.writelines(new_text)
