#Dictionsary
#Dictionary is similar to hash or map as in other langaugaes.
#dictionary values can be accesed from unique key
d=dict()#declare dictionary empty
print(d)
d['naam']="chhoti"
d["pata"]="bihar"
d["gaawn"]="bishnapur"
# iti's alternate ways to declare keys.
print(d)
print(d.keys())#printing onlly keys from dictionart d 
print(d.values())#prinitn only values
#we can delete values and keys using del keyword by key only
print(d["pata"])
del d["pata"]
print(d)
#another ways to declare keys are 
d={"naam":"suruchi","ghar":"mfp"}
print(d)
print("ghar exist in d: ","ghar" in d)
#......
d={"naam":"suru","ghar":"mfp","pin":12}
print(d)
print(len(d))
#convert dictioary into strings using strings
s=str(d)
print(s)
print(s[0:150])
#use items() method to print key value pair of dictionary
print("printing d items: ",d.items())
#use copy function to copy dictionary into some anaother location
d1={}
d1=d.copy()
print("prijting d1 items: ",d1.items())
print("d1 copied as d so clear d: ",d.clear())
print(d.items())
#...........................opearor in python
#for increment and decrement, we don't have x++ or x__ opeeqator,
#we have x+=1and x-=1
#we have '/' it"s a division opeartor and '//' it's a floordivision opeartor.floor division return floor vae like for 2.6, return 2
#to use operator, we must use import operator in python to use add,sub ,mul and many more
import operator
print(operator.add(2,3))
print(operator.mul(2,3))
print(operator.pow(2,3))
print(operator.floordiv(2,3))
print("2 is less than 3: ",operator.lt(2,3))
print("3 is less than or equal to 3: ",operator.le(2,3))
print("3 is equal to 3: ",operator.eq(3,3))
print("2 is less than 3: ",operator.gt(2,3))
print("3 is less than or equal to 3: ",operator.ge(2,3))
print("3 is equal to 3: ",operator.eq(3,3))
 #.............
import operator
l=[1,2,3,4]
l1=["hi"]
print("after setting print list: ",operator.setitem(l,2,4),l)
print("after getting print value: ",operator.getitem(l,2),l)
print("after deeting print list: ",operator.delitem(l,2),l)
print("after setting print list: ",operator.setitem(l,slice(1,3),[21,12]),l)
#above method will update array element using setitem and sllice
#also we can use delete item as above done with setitem using slice
l=operator.concat(l,l1)
print("after setting print list: ",l)
print("after setting print list: ",operator.contains(l,l1))

#counter is subclass of dictionary itself.it is also unordered it can be intialised in 3 ways:
#1.using list as a sequence
#2.using dictinary, key vakues
#3.using keyword arguments
from collections import Counter
c=Counter(['b','c','d'])
c.update([2,3,4])
print(c)
#as dictionary
print(Counter({'A':1,'B':2,'C':3}))
print(Counter(A=1,B=2))
#.........
from collections import Counter
coun=Counter(a=50,b=2,c=3,d=120,e=130,f=219)
for i ,c in coun.most_common(3):
    print(i,": ",c)
#in above, we are using most_common method of counter to print 3 most occuring character from counter coun.
    #...................Iterators
    #let's talk for iterator
#use itertools for iterator uses
import itertools
import operator
list1=[1,2,3,4]
list2=["hii","kammo"]
list3=["tera","pata"]
#here we are adding succesive elemnts in list.
#accumulate iterator takes two arguments always ,one iter function another is normal opearator function like add,sub and many more
print("we can print sum of successiveelemnts of mentioned list: ")
print(list(itertools.accumulate(list1)))#here onlly iter is passed so, be default accumuator terator perform addition of succesve eklemnts
print(list(itertools.accumulate(list1,operator.mul)))
#chain iterator is used to chaining the list means we can combine and put all list values in one through this iterator.
print("prinitng all list elemnts through chain iterator: ")
print(list(itertools.chain(list1,list2,list3)))
#.............
import itertools
li=[2,4,5,7,8,10,20]
li1=[[1,10,5],[8,4,1],[5,4,9],[11,10,1]]
#use islicr to slice the list acc. to NotImplemented
print("rhe sliced list values are: ")
print(list(itertools.islice(li,1,6,2)))

#use starmap() for selection value according to function
#selects min of all tuple values.
print("the values acc. to function are: ")
print(list(itertools.starmap(min,li1)))
#.....................
#takewhile(func,iterable)
#tee(iterator,count)
import itertools
li=[2,4,5,7,8,9,1]
iti=iter(li)
#using takewhile() to print values till conditon is false.
print("the list values till 1st false values are: ",end="")
print(list(itertools.takewhile(lambda x : x%2==0,li)))#so takewhiles se aap tab tak print kar paoge jajb tak kicondition false na ho jaye.
#using tee() to make a list of iterators
#makes list of 3 iterators having same values
it=itertools.tee(iti,3)
#printing values of iterators
print("the iterators are: ")
for i in range(0,3):
    print(list(it[i]))
    #......................
    import itertools
#use iterator product(iter1,iter2) and permutations(iter,groupsize)
#using product,can print cartesian products
print("cartesian product of contaiiners is: ")
print(list(itertools.product('AB','12')))#we can see cartesiam prduct a is getting multiply with 1 then 2,then b with 1 then b with 2
#uing permutations to compute all possible permuutations.
print("all the permutations of the given container is: ")
print(list(itertools.permutations('SKs',3)))
#so we can see using permuation we can find all possible ways to represent above string sks in its size 3.we can change it according to need
#....................................
import itertools
l=[1,2,3]
s=itertools.cycle([1,2,3,4])
print(list(itertools.repeat(25,4)))
#print(list(itertools.count(5,2)))
#we cNan use cycle iterator method to make cycle of any list.
#we canrepeat any number multiple times suing repepat function
