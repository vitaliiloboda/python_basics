with open('text_1.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()

    print(f'The file contains {len(content)} lines.')

    for i, el in enumerate(content, start=1):
        words = el.split()
        print(f'{len(words)} words in {i} line')
