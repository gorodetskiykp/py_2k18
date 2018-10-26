# https://repl.it/repls/YummyNavyblueCamel

path=input("Введите путь к файлу input.txt: ")
text=open(path+"\\input.txt","r").read()
summa=0
numbers=text.split(" ")
for index, number in enumerate (numbers):
    summa=summa+int(number)
open(path+"\\output.txt","w").write(str(summa))
