from defs import new_task, user_shot, set_grade, log_game
from random import randint, choice

shots = 0
errors_num = 0
user_result = ''
difficult = 1
max_difficult = 10

print("Для выхода введите q.\n")

while True:         # проверяем корректность выбора трудости задачи
  dif_input = input('Введите уровень сложности от 1 до 10: ')
  try:
    if 1 <= int(dif_input) <= max_difficult:
      break
    else:
      print('Введите корректное значение...\n')
  except ValueError:
    print('Введите корректное значение...\n')

difficult = int(dif_input)

begin_game = log_game(1)

while True:
    right_result = new_task(difficult) # задаем новую задачку
    exit, user_result = user_shot()    # просим ввести ответ
    if exit:
      end_game = log_game(0)
      break
    else:
      if user_result == right_result: # если ответ правильный
        shots += 1
        print("Правильно!\n")
        log_game(2)
      else:                           # если ответ неверный
        errors_num += 1
        shots += 1
        print("Не правильно!\nПравильный ответ: {}\n".format(str(right_result)))
        log_game(3)

if shots == 0:                    # если нажат сразу выход
  print('Bы не ответили ни на один вопрос!')
  log_game(0)
if shots > 0:                     # подсчитываем результат и ставим оценку
    grade = set_grade(shots, errors_num)
    print("\nВсего ответов: {}\nПравильных ответов: {}\
           \nНеправильных ответов: {}\nОценка: {}".format(
           shots, shots-errors_num, errors_num, grade))
           
log_game(5, begin_game)
     
