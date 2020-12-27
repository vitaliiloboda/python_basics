import json

with open('text_7.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    count = 0
    all_profit = 0
    company_dict = {}

    for line in content:
        company = line.split()
        earnings = int(company[2])
        costs = int(company[3])
        profit = earnings - costs
        if profit > 0:
            count += 1
            all_profit += profit

        company_dict.update({company[0]: profit})

    avg_profit = all_profit / count
    avg_profit_dict = {'average_profit': avg_profit}
    company_list = [company_dict, avg_profit_dict]
    print(company_list)

with open('text_7.json', 'w', encoding='utf-8') as f2:
    json.dump(company_list, f2, indent=4, ensure_ascii=False)
