class Product_card:
    def __init__(self, name, money, amount):
        self.name = name
        self.money = money
        self.amount = amount
    def decrease(self):
       if self.amount<0:
           print('Невозможное количество')
           exit
    def change_mon(self):
        if self.money<0:
           print('Невозможная цена')
           exit
