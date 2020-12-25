class Nucleus():
    def __init__(self, cells):
        self.cells = cells
        self._make_order = ''

    def __add__(self, other):
        return Nucleus(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells - other.cells <= 0:
            return 'вычитание невозможно'
        else:
            return Nucleus(self.cells - other.cells)

    def __mul__(self, other):
        return Nucleus(self.cells * other.cells)

    def __truediv__(self, other):
        if self.cells - other.cells <= 0:
            return 'деление невозможно'
        return Nucleus(self.cells // other.cells)

    def __str__(self):
        return f'{self.cells}'

    @property
    def make_order(self):
        return self.__make_order

    @make_order.getter
    def make_order(self):
        return self._make_order

    @make_order.setter
    def make_order(self, n):
        number_rows = self.cells // n
        el = '\n'.join([''.join('*' for i in range(n)) for j in range(number_rows)])
        add_el = ''.join('*' for i in range(self.cells - (n * number_rows)))
        if self.cells % n == 0:
            self._make_order = f'{el}'
        else:
            self._make_order = f'{el}\n{add_el}'

class Error(Exception):
    pass

class TooSmallValue(Error):
    pass

while True:
    try:
        cells_1 = int(input('Введите количество ячеек в первой клетке: '))
        cells_2 = int(input('Введите количество ячеек во второй клетке: '))
        if cells_1 <= 0 or cells_2 <= 0:
            raise TooSmallValue
        else:
            break
    except TooSmallValue:
        print('Ввод ячеек должен быть положительным числом и содержать хотя бы одну ячейку')
    except ValueError:
        print('Ввод ячеек должен быть целочисленным числом')

nucleus_1 = Nucleus(cells_1)
nucleus_2 = Nucleus(cells_2)
print(f'Результат сложения клеток: {nucleus_1 + nucleus_2}')
print(f'Результат вычитания клеток: {nucleus_1 - nucleus_2}')
print(f'Результат умножения клеток: {nucleus_1 * nucleus_2}')
print(f'Результат деления клеток: {nucleus_1 / nucleus_2}')
nucleus_1.make_order = 5
print(nucleus_1.make_order)