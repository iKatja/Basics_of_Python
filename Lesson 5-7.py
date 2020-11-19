'''Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).'''
import json
profit = {}
loss = {}
av_profit = {}
with open('test_7.txt', 'r') as file_obj:
    for line in file_obj:
        name, ownership, income, costs = line.split()
        if int(income) - int(costs) >= 0:
            profit[f'Вы получили прибыль {ownership} "{name}"'] = int(income) - int(costs)
            av_profit = sum(profit.values()) / len(profit.keys())
        else:
            loss[f'Вы получили убыток {ownership} "{name}"'] = int(income) - int(costs)
with open('test_7.json', 'w') as json_file:
    json.dump(profit, write_js)
    js_str = json.dumps(profit)