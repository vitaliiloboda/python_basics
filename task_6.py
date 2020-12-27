subjects = {}

with open('text_6.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    my_list = content.split('\n')

    for el in my_list:
        new_el = el.split(': ')
        hours_str = new_el[1].split()
        hours_num = []

        for i in hours_str:
            a = ''

            for k in i:
                if k.isnumeric():
                    a = a + k
            if a != '':
                hours_num.append(int(a))

        hours_num_sum = sum(hours_num)

        subjects.update({new_el[0]: hours_num_sum})
    print(subjects)
