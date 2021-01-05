class Typecheck(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    try:
        el = input('Введите число для списка: ')
        if el == 'q':
            break
        try:
            float(el)
        except ValueError:
            raise Typecheck('Тип ввода должен быть числом!')
    except Typecheck as err:
        print(err)
    else:
        my_list.append(el)

print(my_list)
