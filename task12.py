class Student:
    def __init__(self, firstname, secondname,course,grades=[4,5,5,5,5]):
        self.firstname = firstname
        self.secondname = secondname
        self.course = course
        self.grades = grades
    def Middle_me(self,summ):
        for i in range(5):
            summ+=self.grades[i]/5
        print(summ)


student1 = Student("Daniil","Nazarov",1,grades=[4,5,5,5,5])
student1.Middle_me(0)