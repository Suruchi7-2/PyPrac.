#Python supports a special type of method for initillsing data to  instance variable of  a class.
#Whenevr object created ,constructor automaticlly called
#HENce when three instance /object created of a clas sthen three times constructor will be called.
class MObile:
    fp="yes"
    def __init__(self,m,p=500):#formal argument
        self.model=m
        self.price=p
    @classmethod
    def fpmethod(cls):
       return cls.fp

oppo =MObile("Oppo",800)#actual argument
print(oppo.price)
print(MObile.fp)
   # def _init__(self)#default
#Two Types of Variable are there:
#1.instance variable and #anothere is class varaible that is static varaible
#instance varaible is defineds an dintialized using a constuctor .
#instance varaible are those whose separate copy is is created in every object.];
#now focous for class variable which is defined and initialized outside constructor 
#and it is accessing using its class method which should have decorator "@classmethod" and intialized value is accessed using clsvarible just like self as in constructor so always pass cls as aparameter in class method
