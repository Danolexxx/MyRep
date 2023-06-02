try:
    file = open('text.txt', 'r')
except FileNotFoundError:
    print("Файл не найден")
else:
    print("Файл существует")
    file.close()