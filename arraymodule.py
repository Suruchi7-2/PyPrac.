import array #array module
arr=array.array('i',[2,21,3,2,4])#changing list into array using array function of array module
for i in range(0,len(arr)):
    print(arr[i])
arr.append(5)#it will append 5 at last
for i in range(0,len(arr)):
    print(arr[i],end=" ")
print()
arr.insert(0,12)#it will append 12 at position 1 and index 0
for i in range(0,len(arr)):
    print(arr[i],end=" ")
print()
arr.pop(0)#pop always remove out elemnt at specified positon so here at index 0 , elemnt will be popped out
print(arr)
print()
arr.remove(2)#it will remove first occurance of 2 from array
print(arr)
print(arr.index(2))#it will tell index of elemnt 2 
arr.reverse()#it will reverse the array
print(arr)
print("dtatype of above array is: ",arr.typecode)
print("size of this dattype: ",arr.itemsize)
#we can use count function as arr.count(2):it will count no of occurence of 21
#we can use extend fuunction to merger two array into one.
#.................namedtuple
#Namedtuple is similar as dictionary. but it is part of library
import collections
#declaring Namedtuple
father=collections.namedtuple('father',['name','age'])
f=father('sk','55')
#u can acess it using inddex
print("fathers age is : ",f[1])
#u can acess using its anme
print("name: ",f.name)
#.........DEQUEUE AS LIST
#dequeue is as list and most advantage that it does not take muc time to append and pop.mostly it takes o(1) for inserting and o(n) for popping
import collections
dlist=collections.deque([1,2,3,2])
dlist.append(0)
print("printing after appending values 0 at right means at last: ",dlist)
dlist.pop()
print("printing after popping: ",list(dlist))
#we have appendleft method for deque
dlist.appendleft(0)
print("prinitng after inserting 0 at beginning: ",list(dlist))#here 0 added at begining
print("prinitng after removung from left : ",dlist.popleft(),dlist)#here 0 will remove as popleft used
print("prinitng index of values 2: ",dlist.index(2))
print("printing no of occurence of 2: ",dlist.count(2))
print("removing first ocuurence of elemnt 2: ",dlist.remove(2),list(dlist))
#as above we did, u can use insert function to insert values at sepecified position first argu,ment will b eposiiton and second argumen twill be values
#we have ecxtend function to extend multiple deque
dlist2=collections.deque([4,5,6])
dlist.extend(dlist2)
print("printing afetr extending one more deque list: ",dlist)
dlist.extendleft(dlist2)
print(list(dlist))
#we have roatte fuhnction to rotate the deque ,ifin argument number speciiefed will be negative thwn rotation takes place to left. otherwise it will be right
#rotate by 2 to the left
dlist.rotate(-3)
print("deque after rotating  deque 3 times from left: ",dlist)
#rotate by 2 to the right,pass argument positive number
dlist.rotate(2)
print("deque after rotating 2 times  from right : ",dlist)
#we have reverse to reverse deque.
print(dlist.reverse(),dlist)