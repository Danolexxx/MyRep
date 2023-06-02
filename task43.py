try:
    a = int(input('Введите первое: '))
    b = int(input('Введите второе: '))
    result = a/b
    print(result)
except Exception:
    print('Ошибка')
finally:
    exit