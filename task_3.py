with open('text_3.txt', 'r', encoding='utf=8') as f:
    staff = f.readlines()
    min_salary = []
    staff_num = 0
    income = 0
    for el in staff:
        staff_num += 1
        person = el.split()
        income += float(person[1])
        if float(person[1]) < 20000:
            min_salary.append(person[0])
    print(f'Сотрудники у которых оклад меньше 20 тыс.: {min_salary}')
    print(f'Средний доход сотрудиков: {income / staff_num}')

# ***********************************************вариант_2******************************************************

with open('text_3.txt', 'r', encoding='utf=8') as f:
    staff = f.readlines()
    min_salary = []
    persons = {}
    for el in staff:
        persons.update({el.split()[0]: float(el.split()[1])})
    for item in persons:
        if persons.get(item) < 20000:
            min_salary.append(item)

    print(f'Сотрудники у которых оклад меньше 20 тыс.: {min_salary}')
    print(f'Средний доход сотрудиков: {sum(persons.values()) / len(persons)}')
