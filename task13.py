class BankAccount:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance
    def Money_make(self,summ):
        print('Пополнить или снять?(1/0)')1
        if (input()==0)  and ((self.balance-summ)>0):
            self.balance=-summ
        else:
            self.balance=+summ
        print(self.balance)


bankAccount1 = BankAccount("Daniil", 123456738, 1000)
bankAccount1.Money_make(900)