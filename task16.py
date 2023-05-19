class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def say_my_name(self):
        print("Кошка по имени ", self.name,", ",self.age, " лет, ", "цвет ",self.color)
cat1 = Cat("Мурка",7,"белый")
cat1.say_my_name()