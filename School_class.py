class School_class:
    __class_name = ""
    __teachers = []
    __pupils = []

    def __init__(self, class_name):
        self.__class_name = class_name

    def get_class_name(self):
        return self.__class_name

    def add_teacher(self, teacher):
        self.__teachers.append(teacher)

    def add_pupil(self, pupil):
        self.__pupils.append(pupil)

    def get_teachers(self):
        return self.__teachers
        # for teacher in teachers:
        #     print(teacher.get_fullname())

    def get_pupils(self):
        return self.__pupils
        # for pupil in pupils:
        #     print(pupil.get_fullname())

    def __str__(self):
        return self.__class_name
