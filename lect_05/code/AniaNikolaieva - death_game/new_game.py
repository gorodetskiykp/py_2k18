scenes = {
	1: {
		'name': 'Вы проснулись в пустой комнате, в которой две двери. В какую ты выйдешь?',
		'choices': {
			'description': 'Введите 1, чтобы выбрать правую; 2, чтобы выбрать левую',
			1: 2,
			2: 5,
		}
	},
	2: {
		'name': 'Вы попали в комнату, в которой две коробки со змеями. В одной из них ключ от двери. Какую вы выберите?',
		'choices': {
			'description': 'Введите 1, чтобы выбрать правую; 2, чтобы выбрать левую',
			1: 3,
			2: 0,
		}
	},
	3: {
		'name': 'Вы попали в комнату, посреди которой стол. На нем 2 кнопки. Какую вы выберите?',
		'choices': {
			'description': 'Введите 1, чтобы выбрать правую; 2, чтобы выбрать левую',
			1: 4,
			# 2: 0,
            2: 6,
		}
	},
	4: {
		'name': 'Вы попали в комнату, которая наполняется газом.',
		'choices': {
			'description': 'Введите 1, чтобы побежать врепед; 2, чтобы осмотреться',
			1: 1,
			2: 0,
		}
	},
	5: {
		'name': 'Вы оказались в комнате со столом, на котором два стакана, в одном из которых яд.',
		'choices': {
			'description': 'Введите 1, чтобы выбрать правый; 2, чтобы выбрать левый',
			1: 6,
			2: 0,
		}
	},
	6: {
		'name': 'Вы попали в длинный коридор и за вами катится огромный булыжник, но впереди поворот налево.',
		'choices': {
			'description': 'Введите 1, чтобы побежать дальше; 2, чтобы повернуть',
			1: 7,
			2: 0,
		}
	},
	7: {
		'name': 'Булыжник падает в появившемся за вами люке, но в стене открывается дверь, из которой выбегает маньяк с бензопилой. А впереди открывается люк.',
		'choices': {
			'description': 'Введите 1, чтобы перепрыгнуть люк и убежать от маньяка; 2, чтобы прыгнуть в люк',
			# 1: 0,
            1: 5,
			2: 8,
		}
	},
	8: {
		'name': 'Вы попали в комнату с окном и дверью. Через окно вы видите солнечный свет. Что вы выберите?',
		'choices': {
			'description': 'Введите 1, чтобы выбрать окно; 2, чтобы выбрать дверь',
			1: 0,
			2: 'exit',
		}
	},
}

# def get_choice(scene=1):
#     if scene == 0:
#         print("Ты умер!")
#         return
#     if scene == 'exit':
#         print("Ура! Ты нашел выход!")
#         return
#     print(scenes[scene]['name'])
#     while True:
#         try:
#             choice = int(input('{}: '.
#                 format(scenes[scene]['choices']['description'])))
#         except ValueError:
#             choice = 3
#         if choice in [1, 2]:
#             get_choice(scenes[scene]['choices'][choice])
#             return
#         else:
#             print("Всего два варианта! 1 или 2")

def get_choice(scene=1):
    if scene == 0:
        print("Ты умер!")
        return 'exit'
    if scene == 'exit':
        print("Ура! Ты нашел выход!")
        return 'exit'
    print(scenes[scene]['name'])
    while True:
        try:
            choice = int(input('{}: '.
                format(scenes[scene]['choices']['description'])))
        except ValueError:
            choice = 3
        if choice in [1, 2]:
            return scenes[scene]['choices'][choice]
        else:
            print("Всего два варианта! 1 или 2")

# get_choice()

next_step = get_choice()
while True:
    if next_step == 'exit':
        break
    next_step = get_choice(next_step)
