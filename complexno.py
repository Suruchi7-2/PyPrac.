#now, see complex number in python
#we can make any two real number as complex number in python using vomplex function of cmath module.
#complex number in form : X+iY where x an y ARE real no.
import cmath
x=3
y=5
z=complex(x,y)
print(z)
print("printing real part of complex number: ")
print(z.real)
print("printing imaginary part of complex number: ")
print(z.imag)
#we can print ecxponential of z using exp function
print("prinitng exponentia: ",cmath.exp(z))
#as above, we can saMe print log function of z base 2 using log()
print("printing log of z: ",cmath.log10(z,2))
#..............timemodule in python
import time 
#importing time  module
print("Second since epoch: ")
#printing seconds from very first time epoch that is 1stjan 1917.
print(time.time())
print("time calculated according to given seconds: ")
print(time.gmtime())
print(time.ctime())#prints current time
#epoch is very first time from 1st jan 1917.
#....................hcf
#let's find hcf,
#hcf is that largest common factor which divides each numeber mentioned in argument completely. 
#so, while coding it, we will find small number from two number, then try to divide that both number by from 1 till that small no. and when that largest divides both,that will be hcf.
def findhcf(a,b):
    small=min(a,b)
    for i in range(1,small+1):
        if((a%i==0) and (b%i==0)):
            gcd=i 
    return gcd
print("hcf of two number is: ",findhcf(60,48))
#............................
#in python, we have gcd function which is built in frommodule math
import math
print("prinitiing hcf of two number using module functon gcd: ",math.gcd(18,12))
#let'se inpace opearators like iadd and iconcat ,remember to import opearator module
import operator
print(operator.iadd(2,3))
l=["hi"]
l1=["sara"]
print(operator.iconcat(l,l1))
print(operator.imul(4,5))
print(operator.isub(4,5))
#we can print exclusive or using ixor function of inplace operator module
print(operator.ixor(10,5))
#use ipow to find power of xrange
x=2
print(operator.ipow(x,8))
# u can use iand or ior to find and value and or value
#also u can find left and right shift using irshift and ilshift
print(operator.ilshift(8,2))
#basically left shift is like multiplying ur number with 2^no. of shift,like here, 8*2^2,and if it will be right shift i will just divide as in left shift i did multiplying
#...................looping modern technique for not manipulating data structures.
#in python, we have some modern loppimg technique as we don't need to manipulateour ds so  like
#enumerate which will print values with index .
l=[12,2,3,4,5,"hii"]
ans=[12,4,9,16,25]
for i in enumerate(l):
    print(i)
    
#we can use zip function for combining similar two container
for i in zip(l,ans):
    print(i)
#we can use sorted function an reversed functon and these not modifies your data structure only priitng in sorted and reverse order.
for i in sorted(ans):
    print(i,end=" ")
    print()
for i in reversed(ans):
    print(i,end=" ")
#..................random number generator, random module
    #we can generate random number using random module 
import random
l=[10,20,30,40]
print(random.choice(l))#this function will genrate random number from ur mentioned list only.
print(random.randrange(20,100))#trough this we can define to generate random n from 20 till 100
#we can print random numebr between 0 and 1 using random()
print(random.random())
random.seed(2)#so using seed u get fixed random number each time.
print(random.random())
random.shuffle(l)
for i in range(0,len(l)):
    print(l[i])
#using shuffle u can shuffle ur generated list items means u can reorder the elements of list
    #............statistics module in python
import statistics
l=[4,2,6,8]
print("mean of list l: ",statistics.mean(l))
print("prinitng mode of list: ",statistics.mode(l))
print("prinitng median ",statistics.median(l))
#median_grouped() can be used to find 50th percentile,
print("50th percentile of list: ",statistics.median_grouped(l))
#u can calculate variance
print(statistics.variance(l))
print(statistics.stdev(l))#it is calculating standard deviation.