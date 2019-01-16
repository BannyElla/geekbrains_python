# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    series = [1, 1]
    while True:
        new = series[len(series) - 1] + series[len(series) - 2]
        series.append(new)
        if len(series) == m:
            break
    print(series)
    print(series[n-1:])


fibonacci(5, 10)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    sorter_list = []
    for count in range(0, len(origin_list)):
        temp = origin_list[0]
        for element in origin_list:
            if element < temp:
                temp = element
        sorter_list.append(temp)
        origin_list.remove(temp)
    print(sorter_list)

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func, sequence):
    result = []
    for element in sequence:
        if func(element) :
           result.append(element)
    return result


func = lambda x: x % 2 == 0
sequence = [5, 8, 254, 365, 789, 15, 14, 0]
print(my_filter(func, sequence))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
# Если x1+x3=y1+y3 и x2+x4=y2+y4, то ABCD - параллелограмм

def is_parallelogramm(**data):
    x13 = data["x1"] + data["x3"]
    y13 = data["y1"] + data["y3"]
    x24 = data["x2"] + data["x4"]
    y24 = data["y2"] + data["y4"]

    print("x1 + x3 = ", x13)
    print("y1 + y3 = ", y13)
    print("x2 + x4 = ", x24)
    print("y2 + y4 = ", y24)
    if x13 == y13 and x24 == y24:
        return True
    else:
        return False

print(is_parallelogramm(x1 = 5, y1 = 0, x2 = 10, y2 = 30, x3 = 4, y3 = 9, x4 = 6, y4 = -14))
print()
print(is_parallelogramm(x1 = 55, y1 = 75, x2 = -345, y2 = 857, x3 = 41, y3 = 54, x4 = -82, y4 = 0))
