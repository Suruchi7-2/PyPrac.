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