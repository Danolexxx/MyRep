class Person:
    def __init__(self, name, secondname, age, special):
        self.name = name
        self.age = age
        self.special = special
        self.secondname = secondname
    def say_my_name(self):
        print(self.name, " - ", self.secondname, ", ", self.age, "лет, ", self.special)
person1 = Person("Daniil","Nazarov",20,"Webdeveloper")
person1.say_my_name()
