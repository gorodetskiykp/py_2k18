from random import randint, choice
from datetime import datetime

def set_grade(shots, errors_num):
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


def user_shot():
  while True:
    text = input('{} {} '.format("Введите, ответ",'>>'))
    try:
      if text == 'q':
        return True, ''
        #break
      else:  
        a = int(text)
        return False, a
        #break
    except ValueError:
      print('Введите корректный ответ...')


def isInt(n):
    return int(n) == float(n)


def new_task(difficult):
  while True:
    number_1 = randint(1, 10**difficult)
    number_2 = randint(1, 10**difficult)
    operation = choice(['+','-','*','/'])

    request = '{} {} {}'.format(number_1, operation , number_2)
    
    right_result = eval(request)
    
    if operation == '/':
      if isInt(right_result):
        break
    else:
        break

  print("Сколько будет {}?".format(request))
  return right_result


def log_game(log_mark, game_begin_time=0):
  marks_dict = {
    0: 'конец игры',
    1: 'начало игры',
    2: 'дан правильный ответ',
    3: 'дан неправильный ответ',
    5: 'Общее время игры составило',
  }
  time_mark = datetime.now()

  with open('log.txt', 'a') as output_file:
    if log_mark == 5:
      game_time = (time_mark - game_begin_time)
      output_file.write('Общее время игры составило: {} секунд\n\n'.format(game_time.seconds))
    else:  
      output_file.write('{} - {}\n'.format(time_mark.strftime("%Y.%m.%d %H:%M:%S"), marks_dict[log_mark]))
  
  return time_mark
