# Задание
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм. На вход подается число n
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3

"""
В решении задачи были представлены решения в структурной и процедурной реализации.
Структурная от процедурной отличается в обернутости метода. Это значительно облегчает читабельность кода
Так же методы не используют goto.
"""

# Method_1
number = int(input("Введите число: "))
for count in range(1, 10):
    print(number, "x", count, "=", number * count)


count = 1
while count <= 10:
    print(number, "x", count, "=", number * count)
    count += 1


# Method_2
number = int(input("Введите число: "))


def multiplication_table(num):
    for count in range(1, 10):
        print(number, "x", count, "=", number * count)


multiplication_table(number)
