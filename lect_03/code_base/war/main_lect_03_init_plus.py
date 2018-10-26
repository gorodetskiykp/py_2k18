import re

with open("lt1.txt") as wp_file:
    wp_text = wp_file.read()
    # wp_list = wp_text.split(".")
    wp_list_re = re.split(r'[\.!?]+', wp_text)
    # print(len(wp_list))
    # print(len(wp_list_re))
    while True:
        search_word = input('Введите слово для поиска: ')
        search_word = search_word.strip()
        for index, sentence in enumerate(wp_list_re):
            if search_word in sentence:
                print(index, sentence.replace('\n', ' ').strip())
                break
