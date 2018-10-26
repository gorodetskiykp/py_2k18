from math import cos, pi

def fact(n):
    fact_n = 1
    for i in range(1, n+1):
        fact_n *= i
    return fact_n

def abs_x(x):
    return x if x > 0 else x * -1

EPS = 0.000001

x = pi

cos_x = 1

def addend(x, n):
    return (((-1)**n) * (x**(2*n))) / fact(2*n)

n = 1
while True:
    print("n = {}".format(n))
    next_addend = addend(x, n)
    print("next_addend = {}".format(next_addend))
    if abs_x(next_addend) > EPS:
        cos_x += next_addend
        n += 1
    else:
        break

print(cos_x)
print(cos(x))
