class Book:
    def __init__(self, name, author, age, jenre):
        self.name = name
        self.author = author
        self.age = age
        self.jenre = jenre
    def say_my_name(self):
        print(self.name, ", ", self.author, "(", self.age, "), ", self.jenre)
book1 = Book("Десять негритят","Агата Кристи",1968,"детектив")
book1.say_my_name()
