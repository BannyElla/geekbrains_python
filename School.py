from School_class import School_class
from Pupil import Pupil
from Teacher import Teacher
from Mother import Mother
from Father import Father

class School:
    __classes = []

    def print_classes(self):
        for class_name in self.__classes:
            print(class_name.get_class_name())

    def add_class(self, class_obj):
        self.__classes.append(class_obj)

    def print_pupils_by_class(self, class_obj):
        for pupil in class_obj.get_pupils():
            print(pupil.get_full_name())

    def print_teachers_by_class(self, class_obj):
        for teacher in class_obj.get_teachers():
            print(teacher.get_full_name())

    def __str__(self):
        return "I'm a school"

school = School()
mother = Mother("Иванова", "Марья", "Васильевна")
father = Father("Иванов", "Игорь", "Дмитриевич")
pupil_1 = Pupil("Иванова", "Алена", "Игоревна", father, mother)

mother = Mother("Петрова", "Инна", "Евгеньевна")
father = Father("Петров", "Антон", "Николаевич")
pupil_2 = Pupil("Петров", "Олег", "Антонович", father, mother)
mother = Mother("Сидорова", "Ольга", "Петровна")
father = Father("Сидоров", "Иван", "Иванович")
pupil_3 = Pupil("Сидоров", "Петр", "Иванович", father, mother)

teacher_1 = Teacher("Леонтьев", "Дмитрий", "Владимирович", "Химия")
teacher_2 = Teacher("Русакова", "Любовь", "Дмитриевна", "Русский язык")
teacher_3 = Teacher("Алексеева", "Ирина", "Никифоровна", "Математика")
class_7a = School_class("7 A")
class_8b = School_class("8 B")
class_9c = School_class("9 C")

print(class_7a)
print(class_8b)

# class_7a.add_pupil(pupil_1)
# class_8b.add_pupil(pupil_2)
# class_9c.add_pupil(pupil_3)
#
# print(class_1a.get_pupils())

class_7a.add_teacher(teacher_1)
class_8b.add_teacher(teacher_2)
print(class_7a.get_teachers())



school.add_class(class_7a)
school.add_class(class_8b)
school.add_class(class_9c)




