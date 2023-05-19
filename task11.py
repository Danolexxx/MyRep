class Dog:
    def __init__(self, name, type, age):
        self.name = name
        self.age = age
        self.type = type
    def say_my_dog(self):
        print("My dog", self.name, "is", self.type, "and he is", self.age, "y.o.")

dog1 = Dog("Sharik", "labrador", 9)

dog1.say_my_dog()
