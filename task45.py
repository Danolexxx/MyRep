try:
    filename = input("Введите имя файла: ")
    with open(filename, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Файл не найден")
except IOError:
    print("Ошибка при чтении")