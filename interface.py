from abc import ABC ,abstractmethod
class ME(ABC):
    @abstractmethod
    def disp(self):
        pass
class Child(ME):
    def disp(self):
        print("abstract metod efiend but it is interface")
c=Child()

#so INterface is not actally existt explcitly in python.
#but we say interface when we have imprted abc module and then ABC class and absyract method , and then
    #ther is abstarct method declared and no concrete method or normal method is availale then that is interface.
    #we can not create object of interface.
    #we use abstarct when we need same method for different objects lik:
    #in defence force, wheteher army, or navy,or air force they all required same gun that is ak47.
#but it's not same for interface, we use interface where all feathures need to be implemented differently for different objects.
#  .............Difference in ABstract amnd iNterface/...........  
#1.AN abstract class will have abstarct method as well as concrteef method,but all methods of an interface are abstract.abstractmethod
#2.We use abstract class when there are some common fferaures shared by all objects 
#3.while in interface all the fearures need to be implemented differently for different objects.
#4.Use interafce when yiu need to use api.