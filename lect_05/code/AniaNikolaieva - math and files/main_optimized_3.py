FILES_PATH = 'files'

with open('\\'.join([FILES_PATH, "input.txt"])) as numbers_file:
    numbers_text = numbers_file.read()

a, b = tuple(map(int, numbers_text.split()))

with open('\\'.join([FILES_PATH, "output.txt"]), "w") as result_file:
    result_file.write(str(a + b))
