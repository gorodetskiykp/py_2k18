# https://repl.it/@AniaNikolaieva/pog3s

def smert():
  print ("Вы умерли! ")
def exit():
  print ("Вы попали в комнату с окном и дверью. Через окно вы видите солнечный свет. Что вы выберите?")
  a = input ("введите 1 чтобы выбрать окно, 2 чтобы выбрать дверь")
  if ( a== "1"):
    smert()
  else:
    print ("Вы выбрались на свободу!")
    print ("Поздравляю! Вы выжили! Но это не надолго!!!")

while (0 != 1):
  print ("Вы проснулись в пустой комнате, в которой две двери, в какую ты выйдешь?")
  a = input ("Введите 1 чтобы выбрать правую, 2 чтобы выбрать левую")
  if (a == "1"):
    while (1 == 1):
      print ("Вы попали в комнату в которой две коробки со змеями, в одной из них ключ от двери. Какую вы выберите? ")
      a = input ("Введите 1 чтобы выбрать правую, 2 чтобы выбрать левую")
      if ( a == "1"):
          print ("Вы попалив комнату посреди которой стол. На нем 2 кнопки. Какую вы выберите? ")
          a = input ("Введите 1 чтобы выбрать правую, 2 чтобы выбрать левую")
          if ( a == "1"):
            print ("Вы попали в комнату, которая наполняется газом. ")
            a = input ("Введите 1 чтобы побежать врепед, 2 чтобы осмотреться")
            if (a == "2"):
              smert()
          break
      else:
          smert()
      break
    else:
        exit()
        break
  else:
        print ("Вы оказались в комнате со столом, на котором два стакана, в одном из котором яд.")
        a = input ("Введите 1 чтобы выбрать правый, 2 чтобы выбрать левый")
        if ( a == "1"):
          print ("Вы попали в длинный коридор и за вами катится огромный булыжник, но впереди поворот налево")
        a = input ("Введите 1 чтобы побежать дальше, 2 чтобы повернуть")
        if ( a == "1"):
          print ("Булыжник падает в появившемся за вами люке, но в стене открывается дверь из которой выбегает маньяк с бензопилой. А впереди открывается люк.")
          a = input ("Введите 1 чтобы перепрыгнуть люк и убежать от маньяка, 2 чтобы прыгнуть в люк")
          if ( a == "2"):
            exit()
          break
        else:
          smert()
          break
else:
  exit()
