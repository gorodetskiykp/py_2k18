scenes = {
    1: {
        'description' : 'комната, две двери',
        'choices': {
            'description': '1 - направо, 2 - налево',
            1: 2,
            2: 'exit',
        }
    },
    2: {
        'description' : '2 коробки, змея, ключ',
        'choices': {
            'description': '1 - правая, 2 - левая',
            1: 0,
            2: 1,
        }
    },
    0: {
        'description' : 'Вы умерли!',
    },
    'exit': {
        'description' : 'Вы вышли!',
    }
}

# next_step_if_right = some_dict[1]['choices'][1]
# print(some_dict[next_step_if_right]['description'])


def game(scene=1):
    print(scenes[scene]['description'])
    if scene == 0:
        return
    if scene == 'exit':
        return
    while True:
        try:
            choice = int(input(
                '{}: '.format(scenes[scene]['choices']['description'])))
            if choice in [1, 2]:
                break
            else:
                print("Введите 1 или 2")
        except ValueError:
            print("Введите 1 или 2")
    print(choice)
    next_scene = scenes[scene]['choices'][choice]
    game(next_scene)

if __name__ == '__main__':
    game()
