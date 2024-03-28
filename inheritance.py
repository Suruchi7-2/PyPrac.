#whenever we  created classes, so all classeds in python are built from a  single super class that is object object will become super class for them internally.
#Type of Inheritance
#1.Single INheritance
#2.Multilevel Inheritance
#3.Multipple Inheritance
#4Hierarchical INehritance
#if we declare constructor in both classes, then parent class constructor is not acccessible
#which means only child class constructor is accesible.
#and the above situation is called constructor overriding.
#but when u want constructor of parrett class should called then use super method.
class Father:
    def __init__(self):
        print("father class constructor called")
class Son(Father):
    def __init__(self):
        super().__init__()#due to thissuper method in child,now we can acces constructor of parent 
        print("SOn class constructor called")
S=Son()

#Multilevel Inheritance.......
#class Father:
#class son(Father):
#class grandson(son)
#Hierarchical Inheritance.......
#class father:
#class son(father):
#class daughter(father)
#Multiple Inheritance: u know
#class Father:
#class Mother:
#class son(Father,Mother)
class Father:
    def shof(self):
        print("Father class")
class Mother:
    def showm(self):
        print("Mother class method")
class daughter(Father,Mother):
    def showd(self):
        print("DAughter called")
d=daughter()
d.showd()
d.shof()

#in multiple inheritance, when we create object then only it daughter class constructor called
#i want to calle dfathe rclass constructor,so jusut add thqat super().__init__()
#but above ways will only now call fahter class constructor,we need both paent class
#just add that super method inside each class constructor.


