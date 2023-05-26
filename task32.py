class SchoolStudent:
    def __init__(self, name, clas):
        self.name = name
        self.clas = clas
    def study(self):
        print("Школьник ", self.name, " учится в ",self.clas," классе")
SchoolStudent1 = SchoolStudent("Даня", 9)

SchoolStudent1.study()
