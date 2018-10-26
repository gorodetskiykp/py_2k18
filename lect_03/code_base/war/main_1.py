with open('lt1.txt') as wp_file:
    wp_text = wp_file.read()
    wp_list = wp_text.split('.')
    # print(len(wp_list))
    #
    while True:
        search_word = input('Слово: ').strip()
        # print(search_word)
        for sen_index, sentence in enumerate(wp_list):
            if search_word in sentence:
                print(sen_index, sentence.replace('\n', ' ').strip())
                break
