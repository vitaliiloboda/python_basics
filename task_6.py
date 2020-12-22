def int_func(string):
    for i in string:
        if ord(i) > 122 or ord(i) < 97:
            return ''
    return string.title()


def int_func_words(string):
    my_list = []
    words_list = string.split()

    for i in words_list:
        word = int_func(i)
        if word == '':
            continue
        else:
            my_list.append(int_func(i))

    new_string = ' '.join(my_list)

    return new_string


test_word = 'sun'
test_string = 'nice авп ъghj jапро hjjпаро вапрghgh cool'

print(int_func(test_word))
print(int_func_words(test_string))
