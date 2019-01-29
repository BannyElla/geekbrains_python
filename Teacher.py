from Person import Person
class Teacher(Person):
    def __init__(self, lastname, name, surname, lesson):
        Person.__init__(self, lastname, name, surname)
        self.lesson = lesson

    def get_lesson(self):
        return self.lesson
