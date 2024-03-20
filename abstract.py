from abc import ABC, abstractmethod
class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
    def show(self):
        print('Concrete Method')
class Child(Father):
    def disp(self):
        print("Child class abstarct method")
        print("DEfining Abstarct MEthod")
c=Child()
c.disp()
c.show()
#above is example of abstarct method 
#Abstract method is one which is used wile we have parent an d child class. because abstqarct class will 
#have abstract method whcuuh we have to defiine in child class in parent , only declaration is required for abstract method in parent.
#while parent can have concrete method in parent whre abstarct method declared.
#remember we ahve to import ABC class, abstarct method from mkodule name abc