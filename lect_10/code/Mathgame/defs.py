from random import randint, choice
from datetime import datetime

def set_grade(shots, errors_num):
    """Фунцкия выставления оценки.
      Считает отношение числа неправильных ответов к числу попыток и выставляет
      соответствующую оценку
      shots - число попыток.
      errors_num - число неправильных ответов.
      Возвращает string
    """
    errors_prop = errors_num / shots
    if errors_prop == 0:
        grade = '5'
    elif errors_prop < 0.15:
        grade = '5-'
    elif errors_prop < 0.3:
        grade = '4'
    elif errors_prop <= 0.5:
        grade = '3'
    else:
        grade = '2'
    return grade


def new_task(difficult=1):
  """Фунцкия генерирования задания для теста.
    Выбирает случайным образом два числа, операцию между ними, считает
    правильное решение и просит пользователя решить это же задание.
    difficult - сложность задания.
    Возвращает int
  """

  number_1 = randint(1, 10**difficult)
  number_2 = randint(1, 10**difficult)
  operation = choice(['+','-','*','/'])
  if operation == '/':
    number_1 *= number_2
  request = '{} {} {}'.format(number_1, operation, number_2)
  right_result = eval(request)
  print("Сколько будет {}?".format(request))
  return int(right_result)


def log_game(time_mark, user_login, begin_game_time=0, grade=0):
  """Функия генерирования логов для каждого отвечающего.
      :param time_mark - отметка времени для снятия лога.
      :param user_login - логин пользователя, проходящего тест
      :param begin_game_time - время начало прохождения теста
      :param grade - оценка, полученная по результатам теста
      Записывает в файл user_name.txt логи прохождения теста пользователем: время начала прохождения begin_game_time, все ответы пользователя и оценку по итогам прохождения теста grade.
  """
  time_list = {0: 'конец теста', 1: 'начало теста', 2: 'дан правильный ответ', 3: 'дан неправильный ответ', 4: 'общее время теста'}

  time_log = datetime.now()
  name_file = user_login + '.txt'

  with open(name_file, 'a') as output_file:
    if time_mark == 4:
      game_time = time_log - begin_game_time
      output_file.write('Общее время выполнения теста составило: {} секунд\nОценка тестируемого: {}\n\n'.format(game_time.seconds, grade))
    else:
      output_file.write('{} - {}\n'.format(time_log.strftime("%Y.%m.%d %H:%M:%S"), time_list[time_mark]))
      return time_log


def ask_login():
    while True:
      login_input = input('Введите логин (Enter - анонимно): ')
      pass_input = input('Введите пароль (Enter - анонимно): ')
      user_login = check_input((login_input, pass_input), 0)
      if user_login:
        return user_login
      else:
        print('Логин не найден. Введите корректный логин...\n')


def check_login(login, password):
  if login:
      with open('logins.txt') as input_file:
        list_of_logins = input_file.read().split('\n')
      if login in list_of_logins:
        return login    # сверка введенного логина со списком логинов прошла успешно
      else:
        return False    # введенный логин не найден
  else:
      return 'anonimus'

def check_input(user_input, number_of_cheсk):
  if number_of_cheсk == 0:
    login, password = user_input
    login = login.strip()
    password = password.strip()
    return check_login(login, password)

  if number_of_cheсk == 1:
    try:
      difficult = int(user_input)
      if 1 <= difficult <= 3:    # если введенная сложность от 1 до 3х
        return difficult, True
      else:
        return '', False
    except ValueError:
      return '', False

  if number_of_cheсk == 2:
    while True:
      try:
        if user_input == 'q':
          return '', True
          break
        else:
          user_result = int(user_input)
          return user_result, False
          break
      except ValueError:
        print('Неверный ввод...')
        user_input = input('Введите, ответ >>')
