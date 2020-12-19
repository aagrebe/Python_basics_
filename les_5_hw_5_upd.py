import os
path = os.getcwd()

try:
    with open(os.path.join(path, "numbers_5.txt"), "w") as f_obj:
        print("55.3 6.09 22 48.5 16 17.21 78 9.99 67.7", file=f_obj)
    with open("numbers_5.txt") as f_obj:
        numbers = f_obj.read()
        numbers_sum = sum(map(float, numbers.split(" ")))
        print(f'Сумма чисел в файле: {numbers_sum}')
except IOError:
    print("Произошла ошибка ввода-вывода!")