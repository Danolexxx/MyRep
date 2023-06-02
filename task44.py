try:
    file = open('text.txt', 'r',)
except FileNotFoundError:
    print("Файл не найден")
else:
    text = file.read()
    print(text)
    file.close()