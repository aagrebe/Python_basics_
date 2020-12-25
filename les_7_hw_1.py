from random import randrange


class Matrix():
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __add__(self, other):
        first_list = []
        second_list = []
        for i in range(len(self.matrix_list)):
            for j in range(len(self.matrix_list[0])):
                el = self.matrix_list[i][j] + other.matrix_list[i][j]
                first_list.append(el)
                if len(first_list) == len(self.matrix_list[0]):
                    second_list.append(first_list)
                    first_list = []
        return Matrix(second_list)

    def __str__(self):
        return '\n'.join([' '.join(map(str, self.row)) for self.row in self.matrix_list])

    def __eq__(self, other):
        if len(self.matrix_list) == len(other.matrix_list) and len(self.matrix_list[0]) == len(other.matrix_list[0]):
            return True
        else:
            return False

class Error(Exception):
    pass

class TooSmallValue(Error):
    pass

class DifferenSize(Error):
    pass

def m_list():
    while True:
        try:
            column = int(input(f'Введите количество столбцов: '))
            row = int(input(f'Введите количество строк: '))
            m_list = [[randrange(0, 10) for i in range(column)] for j in range(row)]
            if column <= 0 or row <= 0:
                raise TooSmallValue
            else:
                return m_list
        except TooSmallValue:
            print(f'Ввод должен быть больше нуля')
        except ValueError:
            print(f'Ввод должен быть целочисленным')


matrix_1 = Matrix(m_list())
print(matrix_1)
matrix_2 = Matrix(m_list())
print(matrix_2)

try:
    if matrix_1 == matrix_2:
        print(f'Сумма матриц равна: \n'
              f'{matrix_1 + matrix_2}')
    else:
        raise DifferenSize
except DifferenSize:
    print('Матрицы разного размера нельзя складывать')