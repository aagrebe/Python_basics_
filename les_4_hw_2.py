numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(numbers)
numbers_list = (numbers[el] for el in range(1, len(numbers)) if numbers[el] > numbers[el-1])
print(list(numbers_list))