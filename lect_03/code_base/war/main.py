with open('lt1.txt') as wp_file:
    wp_text = wp_file.read()
    wp_list = wp_text.split('.')
    # print(len(wp_list))
    while True:
        search_word = input('Введите слово для поиска: ')
        search_word = search_word.strip()
        for index, sentence in enumerate(wp_list):
            if search_word in sentence:
                print(index, sentence.replace('\n', ' ').strip())
                break
