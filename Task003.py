# Вывести на экран числа от -N до N

from ast import For


def countN(a):
    for i in range(-a, a+1):
        print(i)

countN(5)
