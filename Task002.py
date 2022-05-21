# Напишите программу, которая на вход принимает 5 чисел
# и находит максимальное из них.

def number(a, b, c, d, f):
    if (a > b) and (a > c) and (a > d) and (a > f):
        max = a
    elif (b > c) and (b > d) and (b > f):
        max = b
    elif (c > d) and (c > f):
        max = c
    elif d > f:
        max = d
    else:
        max = f
    print(f"max = {max}")

number(1, 22, 33, 48, 5)

