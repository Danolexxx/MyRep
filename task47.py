try:
    number = float(input("Введите число: "))
    kv = number * number
    print(kv)
except ValueError:
    print("Некорректный ввод")