#All list methods available here
#in and not in keyword in list
#now see len(),max(),min()
l=["surtuci","kumari",12,4]
s=[24,32,45,67]
#len(),min(),max() these are methods of list
print("length of list ",len(l))
print("max element of list: ",max(s))
print("minimum element of list: ",min(s))
#........
l=["surtuci","kumari",12,4]
s=[24,32,45,67]
#see + and * operator in list
# + operator will concatenate two list into 1.
# * opeartor will multiply available list multiply times.
print("use of + in list: ",l+s)
print("use of * in list: ",s*3)
#..........
l=["surtuci","kumari",12,4]
s=[24,32,45,24,67,24]
# see index method and count method of list
print("see index of 24 in l : ",l.index(12))
print("see count of 24 in s : ",s.count(24))
#count method in list return no of occurence of that eleemnt.

#...............
#del( method of list delete elemnt from index mentioned)
l=[23,12,4,5,34,45,67,89]
l1=["suruchi","kumari"]
del l[4:6]
print("return deleted list after deleting: ",l)
#pop just out one elemnt from list.pop need index of elemnt in argument.
print("popping elemnt: ",l.pop(1)," ",l)
#insert will insert elemnt at specified posuton.always remember element  to insert wriiten after wriiten of index.
print("inserting in list 3: ",l.insert(0,3)," ",l)
#remove function always remove the first occurence of element mentioned in argument 
print("removing 3 from list: ",l.remove(3),l)
#sort will sort the lsit while reverse will revere the list in pposite direction
print("reversing list: ",l.reverse(),l)
print("sorting list: ",l.sort(),l)
#extend always add another list elemnt into existeing list.
l.extend(l1)
print("extendiing existing list with another: ",l)
#clear() method of list clear all elemnt.
l1.clear()
print("primtiing empty list l1 after clear method: ",l1)

#...........