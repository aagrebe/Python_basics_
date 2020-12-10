from itertools import cycle
from itertools import count

def func_count(n, q):
    n_count_list = []
    for el in count(n):
        if el > q:
            break
        else:
            n_count_list.append(el)
    return n_count_list

def func_cycle(n, q):
    c = 1
    for el in cycle(n):
        if c > q:
            break
        print(el)
        c+=1

n_cycle = int(input("Введите количество повторений списка: "))
cycle_list = ["geekbrains"]
n_cycle_list = func_cycle(cycle_list, n_cycle)
n_count = int(input("Введите первое число ввода: "))
count_exit = int(input("Введите последнее число ввода: "))
n_count_list = func_count(n_count, count_exit)
print(f'Список чисел от {n_count} до {count_exit} : {n_count_list}')