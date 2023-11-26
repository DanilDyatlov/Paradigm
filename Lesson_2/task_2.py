# Задание 2
# Написать скрипт в любой парадигме, который возвращает полученное число переведенное в двоичную
# систему счисления.

#№1
decimal_num = 8
binary = ""

while decimal_num > 0:
    remainder = decimal_num % 2
    binary = str(remainder) + binary
    decimal_num = decimal_num // 2

print(binary)

#№2
number = int(input('Число в десятичной СС: '))

numberb = ''

while number > 0:
    numberb = str(number % 2) + numberb
    number = number // 2

print(numberb)

#№3
def decimal_to_base(num_dec: int, base: int):
    result = ""
    while num_dec > 0:
        num = num_dec % base
        if num < 10:
            result += str(num)
        else:
            result += chr(num + 55)  # преобразование числа в символ
        num_dec //= base

    return result or "0"


a = 255
b = 16
f = decimal_to_base(a, b)
print(f)