def fact(number):
    num = 1
    if number == 0:
        yield num
    else:
        for i in range(1, number + 1):
            num = num * i
            yield num
number = int(input("Введите число: "))
f = fact(number)
print(list(f))
"""
второй вариант решения, не совсем поняла, хочет ли автор, чтобы было в yield решение факториала или нет
"""
def fact(number):
    for i in range(1, number + 1):
        yield i

number = int(input("Введите число: "))
num = 1
if number == 0:
    print(num)
else:
    for el in fact(number):
        num = num * el
    print(f'Факториал числа {number} - {num}')