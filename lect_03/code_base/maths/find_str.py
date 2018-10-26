import re
some_str = 'qwerty6'
my_str = 'QWERTY'

def checker_1():
    print(my_str)
    my_str = 'ZAQWSX'
    print('- {}'.format(my_str))
    if len(some_str) > 0:
        numbers_count = 0
        for symbol in some_str:
            if symbol.isalnum():
                if symbol.isnumeric():
                    my_number = int(symbol)
                    numbers_count += 1
            else:
                return 'Лишние символы'
        if numbers_count == 1:
            if my_number == len(some_str):
                return 'Цифра равна длине строки'
            else:
                return 'Цифра не равна длине строки'
        elif numbers_count == 0:
            return 'Нет цифр'
        else:
            return 'Слишком много цифр'
    else:
        return 'Строка пустая'

def checker_2(some_str):
    digits = re.findall(r'\d', some_str)
    if len(digits) == 1:
        if int(digits[0]) == len(some_str):
            return 'Цифра равна длине строки'
        else:
            return 'Цифра не равна длине строки'
    elif len(digits) == 0:
        return 'Нет цифр'
    else:
        return 'Слишком много цифр'

# def checker_3(some_str):
#     symbols_list = re.findall(r'\w', some_str)
#
#     print(some_list)

print(my_str)
print(checker_1())
print(my_str)
