class Complex_numbers:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number


number_1 = complex(3, 2)
a = Complex_numbers(number_1)
number_2 = complex(4, 5)
b = Complex_numbers(number_2)
print(f'Результат сложения космлексных чисел {number_1} и {number_2} - {a+b}')
print(f'Результат умножения космлексных чисел {number_1} и {number_2} - {a*b}')