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