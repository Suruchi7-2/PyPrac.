#Let's PAss emmebr of one class to another class
#yes, u can do this using passing object of one class as parameter . creatiion process.
class Student:
    def __init__(self,n,r):
        self.name=n
        self.roll=r
    def show(self):
        print("tudent name is ",self.name)
        print("Student's roll is: ",self.roll)
#Another class
class Teacher:
    @staticmethod
    def display(s):
        print("Teacher name is ",s.name)
        print("Teacher's roll is: ",s.roll)
stu=Student("Suruchi",12)
Teacher.display(stu)#comment
            