#Accessor method or getter method :to get the data Ex:- def get_value(self): it is used to read data of instance variable.
#Mutator/Setter method ir settor method is used to set the data. Ex:- def set_value(self):self.model="samsung"
class MObile:
    def __init__(self):
        self.model="Samsung"
    def get_value(self):
        return self.model
    def set_value(self):
        self.model="oppo"
        return self.model
oppo=MObile()
m=oppo.set_value()
print(m)

#Class Methods:
#methods which act upon class variables. decorator @classmethod need to put while declaring classmethod
#by default 1st paarmeter is cls of class emthod which refers to class itself
# to deal wiith class variable which is outside constructor inside class we have to make class method.
#Class Method without parameter
class Mobile:
    @classmethod#decorator
    def show_model(cls):
        print("REalmex")
real=Mobile()
Mobile.show_model()
#class method can be  accessed using class and object
class MObile:
    fp="yes"

    @classmethod
    def show_model(cls):
        print("FIngerprint: ",cls.fp)
realme=Mobile()
realme.show_model()#here using object is accessed.

#Let's see static method.
#Static method is in process when no  need of class and object. but when some processing is related to the class
class Mobile:
    fp="yes"
    @staticmethod
    def show_model1():
        print("phone is availabe: ",Mobile.fp)
r=MObile()
r.show_model()


