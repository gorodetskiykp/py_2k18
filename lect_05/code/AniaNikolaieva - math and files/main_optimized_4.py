with open('input.txt') as numbers_file:
    numbers_text = numbers_file.read()

a, b = numbers_text.split()

with open('output.txt', 'w') as result_file:
    result_file.write(str(int(a) + int(b)))
