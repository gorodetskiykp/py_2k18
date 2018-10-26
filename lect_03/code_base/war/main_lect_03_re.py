import re

with open("lt1.txt") as wp_file:
    wp_text = wp_file.read()
    wp_list = re.split(r'[.?!]+', wp_text)
    # print(len(wp_list))
    while True:
        search_word_1 = input('Введите первое слово для поиска: ')
        search_word_1 = search_word_1.strip()
        search_word_2 = input('Введите второе слово для поиска: ').strip()
        for index, sentence in enumerate(wp_list):
            if search_word_1 in sentence and search_word_2 in sentence:
                print(index, sentence.replace('\n', ' ').strip())
                break
