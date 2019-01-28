# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import pow
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

class Triangle:
    def __init__(self, pointA, pointB, pointC):
        self.pointA = pointA
        self.pointB = pointB
        self.pointC = pointC

    def get_square(self):
        s = 0.5*((pointA.get_x()-pointC.get_x())*(pointB.get_y()-pointC.get_y())-(pointB.get_x()-pointC.get_x())*(pointA.get_y()-pointC.get_y()))
        return s


    def get_height(self):
        return "Высоту можно вычислить по координатам вершин А({}, {}), B({}, {}), C({}, {})".format(pointA.get_x(), pointA.get_y(),
                    pointB.get_x(), pointB.get_y(),
                    pointC.get_x(), pointC.get_y())

    def get_perimetr(self):
        ab = pow(pow((pointB.get_x() - pointA.get_x()), 2) + pow(pointB.get_y() - pointA.get_y(), 2), 0.5)
        bc = pow(pow((pointC.get_x() - pointB.get_x()), 2) + pow(pointC.get_y() - pointB.get_y(), 2), 0.5)
        ca = pow(pow((pointA.get_x() - pointC.get_x()), 2) + pow(pointA.get_y() - pointC.get_y(), 2), 0.5)
        return ab + bc + ca

pointA = Point(3, 25)
pointB = Point(331, 215)
pointC = Point(0, 81)

triangle = Triangle(pointA,pointB,pointC)
print("S = {}".format(triangle.get_square()))
print("P = {}".format(triangle.get_perimetr()))
print(triangle.get_height())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
from math import pow
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

class Trapeze:
    def __init__(self, pointA, pointB, pointC, pointD):
        self.pointA = pointA
        self.pointB = pointB
        self.pointC = pointC
        self.pointD = pointD
        self.ab = pow(pow((pointB.get_x() - pointA.get_x()), 2) + pow(pointB.get_y() - pointA.get_y(), 2), 0.5)
        self.bc = pow(pow((pointC.get_x() - pointB.get_x()), 2) + pow(pointC.get_y() - pointB.get_y(), 2), 0.5)
        self.cd = pow(pow((pointD.get_x() - pointC.get_x()), 2) + pow(pointD.get_y() - pointC.get_y(), 2), 0.5)
        self.da = pow(pow((pointA.get_x() - pointD.get_x()), 2) + pow(pointA.get_y() - pointD.get_y(), 2), 0.5)

    def check(self):
        return self.ab == self.cd or self.bc == self.da

    def get_square(self):
        return "Высоту трапеции можно вычислить по координатам вершин А({}, {}), B({}, {}), C({}, {}), D({}, {})".format(pointA.get_x(), pointA.get_y(),
                    pointB.get_x(), pointB.get_y(),
                    pointC.get_x(), pointC.get_y(),
                    pointD.get_x(), pointD.get_y(),)

    def get_height(self):
        return "Высоту трапеции можно вычислить по координатам вершин А({}, {}), B({}, {}), C({}, {}), D({}, {})".format(pointA.get_x(), pointA.get_y(),
                    pointB.get_x(), pointB.get_y(),
                    pointC.get_x(), pointC.get_y(),
                    pointD.get_x(), pointD.get_y(),)

    def get_perimetr(self):
        return self.ab + self.bc + self.cd + self.da

pointA = Point(3, 25)
pointB = Point(331, 215)
pointC = Point(0, 81)
pointD = Point(328, 271)
trapeze = Trapeze(pointA, pointB, pointC, pointD)
print(trapeze.check())
print(trapeze.get_square())
print(trapeze.get_height())
print(trapeze.get_perimetr())

# Если было бы дано не две разные задачи, а одна с условием создать классы двух фигур, тогда можно было бы создать
# родительский класс Figure, от которого отнаследовать треугольник и трапецию. В Figure вынести метод определения длины стороны.
# Если стороны вносить в список, тогда вычисление периметра тоже можно вынести в Figure

