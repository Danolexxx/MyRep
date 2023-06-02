try:
    with open("test.txt", "w") as file:
        file.write("Hello, world!")
except IOError:
    print("Ошибка")
    exit