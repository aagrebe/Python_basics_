class Complex_numbers:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number


number_1 = Complex_numbers(complex(3, 2))
number_2 = Complex_numbers(complex(4, 5))
print(f'Результат сложения комлексных чисел {number_1.number} и {number_2.number} - {number_1+number_2}')
print(f'Результат умножения комлексных чисел {number_1.number} и {number_2.number} - {number_1*number_2}')
