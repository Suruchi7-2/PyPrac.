#bisect algorithm in python helps to insert new element in sorted list.like it returns an index where that element should be in sorted list
import bisect
#bisect() function takes 4 arguments like list,number,beg=0,end=len(list)
l=[1,3,4,4,4,6,7]
print("the rightmost index to insert , so list remains sorted: ",bisect.bisect(l,4))
#wd can use bisect_left to find out leftmost index in sorted list
print("the leftmost index to insert 4 : ",bisect.bisect_left(l,4))
#now , we have insort() function through which elemnt at appropriate position is inserted,it also takes 4 arguments
bisect.insort(l,4)
print("After insertion of 4 our list looks like they will hv four 4: ",l)
bisect.insort_left(l,5)
print("inertion of 5 : list will be: ",l)
#..................we have FILE ACCESS MODES
#1.Read only=use 'r'
#2.Read and Write=use 'r+'

#3write only= use 'w'
#4write and read = use 'w+'
#5append only=use 'a'
#6appned and read= use 'a+'

#...........CSV files are comma separated values which generally used to store tabular data or spreadsheet or database
#we can read csv files means can extract dat from csv and also can write data into csv.
#we can find permutation and combination using its modules
l=[1,2,3,4]
l1=[1,2,3]
from itertools import permutations
perm=permutations(l)#4P4
for i in list(perm):
    print(i)
#so, in above we saw how n! is founded by permuattion of 4 elemnt.
#now we will passeds arguments as length for permuutation
perm1=permutations(l1,2)#only 10 element got printed as permuation would be: 3P2
for i in list(perm1):
    print(i)
from itertools import combinations
comb=combinations(l1,2)#only  6 gets printed.as 3C2
print("Combinatins are : ")
for i in list(comb):
    print(i)
#.......KEYWORD
#keyword is built in python tool, we can't use keyword as a varaible
#let's check for atsrig is keyword or not
import keyword
s="for"
print("for is keyword: ",keyword.iskeyword(s))
#u can also print each and every keyword in python using kwlist
print("the list of keywords are: ",keyword.kwlist)
#so total we have 33 no of keywords
#..........
#we have deep copy theory when any chnages on copy of list doesn't effect previously existed list
#means if we make copy of list l1 that is l2 then chnages made in l2 doesn't effect l1 means changes inly reflect n l2 not in l1
#while in shallow, as , we pass reference emans when copy of l1 that is l2 makes then in actual l2 will pount to l1 location and hence any changes in l2 will also reflect in l1.
#........................
#we can find permutation and combination using its modules
l=[1,2,3,4]
l1=[1,2,3]
from itertools import permutations
perm=permutations(l)#4P4
for i in list(perm):
    print(i)
#so, in above we saw how n! is founded by permuattion of 4 elemnt.
#now we will passeds arguments as length for permuutation
perm1=permutations(l1,2)#only 10 element got printed as permuation would be: 3P2
for i in list(perm1):
    print(i)
from itertools import combinations
comb=combinations(l1,2)#only  6 gets printed.as 3C2
print("Combinatins are : ")
for i in list(comb):
    print(i)
#.......KEYWORD
#keyword is built in python tool, we can't use keyword as a varaible
#let's check for atsrig is keyword or not
import keyword
s="for"
print("for is keyword: ",keyword.iskeyword(s))
#u can also print each and every keyword in python using kwlist
print("the list of keywords are: ",keyword.kwlist)
#so total we have 33 no of keywords
#facts for strings..........
#Strings is  immutable in python
#like we can't modiifed it onceassigned
#we can't use index assignment to modift
#$we can use + operatort o concat but in actual ,it will reassign another variable in which string get  odified. id doesn't modifies the created string
#print single quote or double quote 
str2='hiii this is "usuruchi"'
print(str2)
str1="hey,what's ur 'name'"
print(str1)
#we4 have problem where u have to count frequencies of each element present in list
arr=[1,1,1,1,2,2,2,2,3,3,4,5,5]
count1={}
for i in arr:
    if i in count1:
        count1[i]+=1 
    else:
        count1[i]=1
print(count1)
#above apprach takes o(n) time and space o(n),hence use counter function of module collections
from collections import Counter#we know counter is subclass of dictionary,it is giving count values of each eelmnt in dictonary form.
arr=[1,1,1,1,2,2,2,2,3,3,4,5,5]
s=Counter(arr)
for i,j in s.items():
    print(i,"=",j)
#convert list to string
    #now I ahve one question in which character are given in list and i have  to convert into basestring
l=['s','u','r','u','c','h','i']
str1=""
for i in l:
    str1+=i 
print(str1)
#another approach using join
str2=""
print(str2.join(l))
#reverse stringcode
s="suruchi"
t=""
for i in range(len(s)-1,-1,-1):
    t=t+s[i]
print(t)
 #u can use reversed keyword too 
#reverse stringcode
s="suruchi"
t=""
for i in range(len(s)-1,-1,-1):
    t=t+s[i]
print(t)
print("".join(reversed(s)))#use reversed function
#use extended slicing
modified=s[::-1]
print(modified)
