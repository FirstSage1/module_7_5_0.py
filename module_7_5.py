    # Модуль 7_5. "Файлы в операционной системе".
    # ==================================================
import os
import time

print(os.getcwd()) # отображение пути к файлу в котором мы сейчас находимся
directory = '.'     # текущая директория
for root, dirs, files in os.walk(directory): #walk() генерирует имена файлов
                                            # в дереве каталогов, обходя дерево
                                    # root-имя переменной, которая обозначает корневое окно
    for file in files:
        filepath = os.path.join(root, file)      # конкатенацию (склеивание) пути path
        filetime = os.path.getmtime(filepath)  # время последнего изменения файла в виде числа
        # с плавающей точкой, представляющего секунды с начала эпохи (обычно это 01.01.1970 г.).
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime)) # преобразование
                                            # времени файла в сироку с нужными нам параметрами
        filesize = os.path.getsize(filepath) # размер файла в байтах
        parent_dir = os.path.dirname(filepath) # возвращает имя
                        # родительской директории файла по указанному пути.

    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')