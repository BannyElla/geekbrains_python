class Person:
    def __init__(self, lastname, name, surname):
        self.name = name
        self.surname = surname
        self.lastname = lastname

    def get_full_name(self):
        return "{} {} {}".format(self.lastname, self.name, self.surname)

    def __str__(self):
        return "{} {} {}".format(self.lastname, self.name, self.surname)
