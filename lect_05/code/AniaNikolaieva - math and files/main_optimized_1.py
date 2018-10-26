path = input("Введите путь к файлу input.txt: ")

with open('\\'.join([path, "input.txt"])) as numbers_file:
    numbers_text = numbers_file.read()

sum = 0
numbers = numbers_text.split()
for number in numbers:
    sum = sum + int(number)

with open('\\'.join([path, "output.txt"]), "w") as result_file:
    result_file.write(str(sum))
