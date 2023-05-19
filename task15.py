class Car:
    def __init__(self, mark, model, age, cost):
        self.mark = mark
        self.model = model
        self.age = age
        self.cost = cost
    def say_my_name(self):
        print(self.mark, " - ", self.model, ", ", self.age, ", ", self.cost)
car1 = Car("Tesla","NT-1223",2019,18500000)
car1.say_my_name()
