# import settings
from defs import new_task, set_grade, log_game, check_input, ask_login


shots = 0
errors_num = 0
user_result = ''
# difficult = 1
max_difficult = 3

if __name__ == "__main__":

    print("Для выхода введите q.\n")

    user_login = ask_login()

    while True:         # проверяем корректность выбора трудости задачи
      dif_input = input('Введите уровень сложности от 1 до 3: ')
      difficult, flag = check_input(dif_input, 1)
      if flag:
        break
      else:
        print('Введите корректное значение...\n')

    begin_game = log_game(1, user_login , 0, 0)

    while True:
        right_result = new_task(difficult) # задаем новую задачку
        user_input = input('Введите, ответ >> ')
        user_result, exit = check_input(user_input, 2)   # просим ввести ответ
        if exit:
          log_game(0, user_login, 0, 0)
          break

        if user_result == right_result: # если ответ правильный
          shots += 1
          print("Правильно!\n")
          log_game(2, user_login, 0, 0)
        else:                           # если ответ неверный
          errors_num += 1
          shots += 1
          print("Не правильно!\nПравильный ответ: {}\n".format(str(right_result)))
          log_game(3, user_login, 0, 0)

    if shots == 0:                    # если нажат сразу выход
      print('Bы не ответили ни на один вопрос!')
      #log_game(0, user_login, 0, 0)
      grade = 2
    if shots > 0:                     # подсчитываем результат и ставим оценку
        grade = set_grade(shots, errors_num)
        print("\nВсего ответов: {}\nПравильных ответов: {}\
               \nНеправильных ответов: {}\nОценка: {}".format(
               shots, shots-errors_num, errors_num, grade))

    log_game(4,user_login, begin_game, grade)
