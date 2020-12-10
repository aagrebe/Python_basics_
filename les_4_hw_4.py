numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f'Исходный список: {numbers}')
new_list = (el for el in numbers if numbers.count(el) == 1)
print(f'Неповторяющиеся элементы списка: {list(new_list)}')