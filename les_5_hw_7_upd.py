import os
import json
path = os.getcwd()

def average_profit(dict):
    sum = 0
    n = 0
    for el in dict.values():
        if el > 0:
            n += 1
            sum += float(el)
            mid_profit = sum / n
    return round(mid_profit, 2)

text_dict = {}
try:
    with open(os.path.join(path, "firm_7.txt")) as f:
        for line in f:
            print(line)
        f.seek(0)
        text = f.read()
        text_list = [el.split(' ') for el in text.split('\n')]
        for el in text_list:
            profit = float(el[2]) - float(el[3])
            text_dict.update({el[0]: round(profit, 2)})
        text_dict.update({"average_profit": average_profit(text_dict)})
        print(text_dict)
    with open(os.path.join(path, "firm_7.json"), "w") as j:
        json.dump(text_dict, j)
except IOError:
    print("Произошла ошибка ввода-вывода!")