from defs import set_grade
from random import randint, choice

shots = 0
errors_num = 0
user_result = ''
difficult = 1

print("Для выхода введите q.\n")

difficult = int(input('Введите уровень сложности: '))

while True:
    if user_result == 'q':
        break
    number_1 = randint(1,10**difficult)
    number_2 = randint(1,10**difficult)
    request = '{} {} {}'.format(number_1, choice('+-*'), number_2)
    print("Сколько будет {}?".format(request))
    right_result = eval(request)
    while True:
        user_result = input()
        if user_result != 'q':    
            if user_result.isnumeric():
                shots += 1
                if int(user_result) == right_result:
                    print("Правильно!\n")
                    break
                else:
                    errors_num += 1
                    print("Не правильно!\nПравильный ответ: {}\n".format(
                           str(right_result)))
                    break
            else:
               continue
        else:
            break

if shots > 0:
    grade = set_grade(shots, errors_num)
    print("\nВсего ответов: {}\nПравильных ответов: {}\
           \nНеправильных ответов: {}\nОценка: {}".format(
           shots, shots-errors_num, errors_num, grade))
     
