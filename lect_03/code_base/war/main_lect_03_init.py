from re import split as re_split

with open("lt1.txt") as wp_file:
    wp_text = wp_file.read()
    wp_list = re_split(r'[\.!?]+', wp_text)
    while True:
        search_word_1 = input('Введите 1 слово для поиска: ').strip()
        search_word_2 = input('Введите 2 слово для поиска: ').strip()
        for index, sentence in enumerate(wp_list):
            if search_word_1 == search_word_2 and \
                    sentence.count(search_word_1) >= 2:
                print(index, sentence.replace('\n', ' ').strip())
            elif search_word_1 != search_word_2 and \
                search_word_1 in sentence and search_word_2 in sentence:
                print(index, sentence.replace('\n', ' ').strip())
        break
