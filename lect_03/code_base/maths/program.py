import math
from math import pi as PI

from fct import fct_function

def chislit(x, n):
    return ((-1)**n) * (x**(2*n))

def next_number(x, n):
    return chislit(x, n) / fct_function(2*n)

def modul(x):
    return x if x > 0 else (-1) * x

if __name__ == '__main__':
    result = 1
    n = 0
    x = float(input('Введите x: '))
    eps = float(input('Введите eps: '))
    while True:
        n += 1
        next_x = next_number(x, n)
        if modul(next_x) > eps:
            result += next_x
        else:
            break
    print('Наша функция: {}'.format(result))
    print('Функция math: {}'.format(math.cos(x)))
