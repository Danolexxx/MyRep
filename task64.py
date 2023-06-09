class Client:
    def __init__(self,name, money, tranz):
        self.name = name
        self.money = money
        self.tranz = tranz       
class Bank:
    def __init__(self, client_Baze=[]):
        self.client_Baze = client_Baze
    def addClient(self,client):
        self.client_Baze.append(client)
    def tranzact(self, sum, guy, guy2):
        print('Введите сумму отправления:')
        input(sum)
        print('Веедите от какого клиента отправить деньги(начиная с 0):')
        input(guy)
        print('Веедите какому клиенту отправить деньги(начиная с 0):')
        input(guy2)
        if (self.client_Baze[guy]).money<sum:
            print('недостаточно средств')    
            exit
        if (guy<0) or (guy>len(self.client_Baze)):
            exit
        if  (guy2<0) or (guy2>len(self.client_Baze)):
            exit 
        else:
            (self.client_Baze[guy]).money-=sum
            (self.client_Baze[guy2]).money+=sum