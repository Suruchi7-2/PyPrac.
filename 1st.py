class Student:
    def __init__(self,name,address):#use self for attribute it is same as this used to use anothere name of attribute /variabkle in class
        self.naam=name#like name is defined but we used another name for name as naam.
        self.pata=address
        #now add function to defined behaviour of above class like function 
    def studetail(self):
        return f"Name: {self.naam}, Address: {self.pata}"



mystud=Student("Suruchi","Bihar")#instance mystud .when it created above constructor called itsdelf.
print(mystud.naam)#way to print attribute or variable using dot.
mystud1=Student("ANupriya","Bihar")
store= mystud1.studetail()
print(store)

#let's inherit teacher from student with new feature salary.
class Teacher(Student):
    def __init__(self,name,address,salary):
        super().__init__(name,address)
        self.kamai=salary
 #so basically object of techer can acces student function or varaible using super method.  
       
tecaher1=Teacher("Sakshhi","p","45k")
store1=tecaher1.studetail()
print(store1)
print(tecaher1.kamai)

