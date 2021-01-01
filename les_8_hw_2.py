class Zerocheck(Exception):
    def __init__(self, txt):
        self.txt = txt


def number_check(num_1, num_2):
    try:
        if num_2 == 0:
            raise Zerocheck('Деление на ноль запрещено!')
    except Zerocheck as err:
        print(err)
    else:
        return round(num_1/num_2, 2)

while True:
    try:
        number_1 = float(input('Введите первое число, будем делить числа: '))
        number_2 = float(input('Введите второе число, не ноль(!): '))

    except ValueError:
        print('Тип ввода должен быть числом!')
    else:
        break

div = number_check(number_1, number_2)
if div is not None:
    print(f'Результат деления чисел: {div}')