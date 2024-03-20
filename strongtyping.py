#hasattr() fnction is used to check whether the object has a method or not,if it's found then return true otherwise false.
#like  while in ducktyping, there is no ned to check hether that method is prrsent inside  that object clas  or not, but here we chheck
class Duck:
    def walk(self):
        print("duck")
class Horse:
    def walk(self):
        print("Horse")
def myfunction(self):
    if(hasattr(self,"walk")):
         self.walk()
d=Duck()
myfunction(d)

#MEthod overloading:Python should not  have same name of emthods in one class, 
#henc here, method overloading is different from others.
#IN python,if a method is written in such a way that it can perform more than one task.and that is method overloadinfg
class Hyy:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a*b
        else:
            s="Provide atleast two numbers"
        return s
obj=Hyy()
print(obj.sum(43,12))
          
#Method Overridng. MEthod overridng is same as constructor overriding.
#like for method, metod overriding, base and derived class should be. 
#like when same namemethod is defined in base and derived , then only derived class method is calling when object of derived class is calling that same method.
#so, we try to call parent method too ,hence use super(). method.

class Add:#Base class
    def result(self,x,y):
        print("Addition: ",x+y)
class Multi(Add):#Derived class.
    def result(self,a,b):
        super().result(10, 20)#due tot his, parent class method also called but always passed actual argument here.
        print("Multiplication: ",a*b)
m=Multi()
m.result(10,20)

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}j"

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imag - other.imag)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            # Complex number multiplication formula
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return ComplexNumber(real_part, imag_part)
        elif isinstance(other, (int, float)):  # Allow multiplication by scalars
            return ComplexNumber(self.real * other, self.imag * other)
        else:
            return NotImplemented
