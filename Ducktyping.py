#polymorphism have types:
#Duck Typing
#Operator Overloading
#MEthod Overloading
#MEthod Overriding
#...........Duck typing................
# So, pyhton says,if horse walks like a duck or speak like a duch means it behaviour like a  duck while ther are not duck,yet we will consider horse like a duck
#means python doesn't care about which class of objecjt is , if it is an object and required behaviour is present for that object then it will work
#the type of object is  diferenced at runtime only that is duck typing
class Duck:
    def walk(self):
        print("thapak thapakp thapak thapak")
class Horse:
    def walk(self):
        print("tabdak tabdak tabdk tabdak")
def myfunction(self):
    self.walk()
d=Duck()
myfunction(d)
h=Horse()#so this object deosn't bother a little bit about of whcih class it is.
myfunction(h)
# comment