FILES_PATH = 'files'

with open('\\'.join([FILES_PATH, "input.txt"])) as numbers_file:
    numbers_text = numbers_file.read()

numbers = map(int, numbers_text.split())
numbers_sum = str(sum(list(numbers)))

with open('\\'.join([FILES_PATH, "output.txt"]), "w") as result_file:
    result_file.write(numbers_sum)
