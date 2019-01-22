# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

# Создание дирректории
root_dir = os.getcwd()
print(root_dir)
for i in range(1, 10):
    dir_name = 'dir_' + str(i)
    dir_path = os.path.join(root_dir, dir_name)
    try:
        os.mkdir(dir_path)
        print("Дирректория {} создана".format(dir_name))
    except FileExistsError:
        print('Такая директория уже существует')

print()

# Удаление дирректории
for i in range(1, 10):
    dir_name = 'dir_' + str(i)
    dir_path = os.path.join(root_dir, dir_name)
    try:
        os.rmdir(dir_path)
        print("Дирректория {} удалена".format(dir_name))
    except FileNotFoundError:
        print('Такая директория не существует')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os

current_dir = os.getcwd()
dir_list = filter(lambda x: os.path.isdir(os.path.join(current_dir, x)), os.listdir(current_dir))
print(list(dir_list))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil
import os

current_file = __file__
root_dir = os.getcwd()
new_file = os.path.join(root_dir, "new_file.py")
try:
    shutil.copy2(current_file, new_file)
    print("Файл {} был создан".format(new_file))
except IOError:
    print("Произошла ошибка при копировании файла")
