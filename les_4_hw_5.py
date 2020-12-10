from functools import reduce
number_list = (el for el in range(100, 1001) if el % 2 == 0)
multiply_list = list(number_list)
print(f'Четные числа от 100 до 1000: {multiply_list}')
multiply = reduce(lambda x , y: x * y, multiply_list)
print(multiply)