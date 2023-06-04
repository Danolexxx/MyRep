import glob
import os

def found_file(path, extension):
    if not os.path.exists(path):
        return print('Ошибка, не найдено')
    files = glob.glob(path + '**/*.' + extension, recursive=True) 
    return print(files)                                           

path1 = input('Введите путь:')
extension1 = input('Введите расширение: ')
found_file(path1, extension1)