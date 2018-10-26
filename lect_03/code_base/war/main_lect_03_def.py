import re

def file_to_list(file_name):
    with open(file_name) as file_desc:
        file_text = file_desc.read()
        return re.split(r'[\.?!]+', file_text)

def find_sentences(init_list, search_word_1, search_word_2):
    for sen_index, sentence in enumerate(init_list):
        if search_word_1 in sentence and search_word_2 in sentence:
            return True, sen_index, sentence.replace('\n', ' ').strip()
    return False, '', ''

def main():
    wp_list = file_to_list("lt1.txt")
    search_word_1 = input('Введите первое слово для поиска: ').strip()
    search_word_2 = input('Введите второе слово для поиска: ').strip()
    result, sen_index, sentence = find_sentences(wp_list, search_word_1, search_word_2)
    if result:
        return sen_index, sentence
    else:
        return 'Ничего нет'


if __name__ == '__main__':
    i, sen = main()
    print(i)
