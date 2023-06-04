class Homework:

    def __init__(self):
        with open('home.txt', 'r', encoding='utf-8') as file:
            self.stroke= file.read()
            file.close()

    def addEL(self, string):
        with open('home.txt', 'a', encoding='utf-8') as file:
            file.writelines(string + '\n')
            file.close()
        return

    def deleteEL(self, index):
        with open('home.txt', 'r') as file:
            stroke = file.readlines()
            del lines[index]
            file.close()
        with open('home.txt', 'w') as file:
            file.writelines(stroke)
            file.close()
        return

    def printALL(self):
        return print(self.lines)

my_list = Homework()

my_list.addEL("To wash the dishes")
my_list.deleteEL(1)
my_list.printALL()