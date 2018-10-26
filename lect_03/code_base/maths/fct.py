def fct_function(n):
    """
    Функция для вычисления факториала от n
    Вход: целое число
    Выход: факториал числа
    """
    result = 1
    for x in range(n):
        result = result * (x + 1)
    return result

if __name__ == '__main__':
    print(fct_function(5) == 1*2*3*4*5)
