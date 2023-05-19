class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_my_name(self):
        print("My name is", self.name, ",I am",
        self.age, "y.o.")
person1 = Person("Daniil", 20)
person1.say_my_name()
