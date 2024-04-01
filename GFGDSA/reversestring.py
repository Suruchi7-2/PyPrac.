#Approach1:use slicing :: double colon means starts from 0 and end at n, ,-1 means direction is reverse.
def reverse_string(s):
    k=s[::-1]
    print(k)
reverse_string("Suruchi Kumari")
#Approach 2 for reversing string: use reverse function
#as reverse function only aply on list so firstly convert string into list.
#use join as reverse will return revrse string in list format where each character of string will be stored in list, so use join to join that character.
def reverse_string(s):
    l=list(s)
    l.reverse()
    print("".join(l))
reverse_string("hi")

#Qs...print sum of maximum and minimum elements of array.
class solution:
    def sum_maxmin(self,a,n):
        if n==1:
            return a[0]
        if a[0]>a[1]:
            max=a[0]
            min=a[1]
        else:
            max=a[1]
            min=a[0]
        for i in range(2,n):
            if(a[i]>max):
                max=a[i]
            elif(a[i]<min):
                min=a[i]
        print(max+min)
s=solution()
a=[2,3,1,4]
n=4
s.sum_maxmin(a,n)
#u can use here max and min function too for fniidng min and max.
#Qs: GIven an array[] and an integer k,where k is smaller than size of array,task is to find out thekth smallest eleemnt in given array,it is given array element is distinct.
#so basically like if k is 3 in qs, then find 3rs smallest  elemnt from array.
class solution:
    def findksmallest(self,a,k):
        if len(a)==1:
            return a[0]
        else:
            a.sort()
            print(a[k-1])
s=solution()
a=[78,34,12,34,11,67,23]
k=3
s.findksmallest(a,k)
#qs....just use this to find asceending order of array elements without function
arr = [34, 22, 14, 12, 10]
n = len(arr)  # Get the length of the array
for i in range(n-1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
print(arr)

#Qs...given an array which consists of 0,1 and 2 .sort the array without using any sorting algorithm.
#sort function in python have time compplexity n(log n),so in this don;t suse that.because we need solutin in o(n)
#arr[]={0,2,1,2,0},n=5
arr=[0,2,1,2,0]
n=5
c0=0 
c1=0 
c2=0 
for i in range(n):
    if arr[i]==0:
        c0+=1 
    elif arr[i]==1:
        c1+=1 
    elif arr[i]==2:
        c2+=1 
#now here logic is that in above we have countable 0,1 and 22
#nw we will put 0 first then 1 and then 2
i=0 
while(c0>0):
    arr[i]=0 
    i+=1 
    c0-=1 
while(c1>0):
    arr[i]=1 
    i+=1 
    c1-=1 
while(c2>0):
    arr[i]=2 
    i+=1 
    c2-=1 
print(arr)
