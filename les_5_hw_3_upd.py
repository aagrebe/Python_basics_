def average_salary(dict):
import os
path = os.getcwd()

def average_salary(dict):
    text_list = list(dict.values())
    mid_salary = sum(map(float, text_list)) / len(text_list)
    return round(mid_salary, 2)

try:
    with open(os.path.join(path, "salary_3.txt")) as workers_salary:
        text = workers_salary.read()
        text_dict = dict(el.split(" ") for el in text.split("\n"))
        biggest_salary = [key for key, value in text_dict.items() if float(value) > 20000]
        print(f'Зарплата более 20 тысяч у следующих сотрудников: {" ".join(biggest_salary)}')
        mid = average_salary(text_dict)
        print(f'Средняя зарплата сотрудника - {mid}')
except IOError:
    print("Произошла ошибка ввода-вывода!")