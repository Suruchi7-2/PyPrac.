class Animal:
    #Encapsulation is to encapsulate data memebr on is own. like private meber is of unction only so noone one can acces it.
    total=0
    def __init__(self,legs1,head1,tail):
        self.legs1=legs1
        self.head1=head1
        self.__tail=tail
        Animal.total+=1
    def detail(self):
        return f"Legs={self.legs1}, Head={self.head1}, Tail={self.__tail}"
    def factor(self):
        return f"Animal is it"
class Dog(Animal):
    def __init__(self,legs1,head1):
        super().__init__(legs1,head1,tail=2)
    def factor(self):
        return f"DOg is it"
an=Animal(4,1,1)#so any object can't acces private variable but function have accessability only.
store=an.detail()
print(store)
print(an.factor())
#POlymorphism is having multiple form of same things like above function factor in both class, same thing factor is but prpinting differen things.
d=Dog(2,1)
store1=d.detail()
print(store1,d.factor())
print(Animal.total)

# due to double underscore any variable become private and hence any object if that can't access that private memnber. only class can accessprint(an.__tail)