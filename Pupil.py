from Person import Person
class Pupil(Person):
    def __init__(self, surname, name, lastname, father, mother):
        Person.__init__(self, surname, name, lastname)
        self.father = father
        self.mother = mother

    def get_parents(self):
        return "Отец: {}\nМать: {}".format(self.father.get_full_name(), self.mother.get_full_name())
