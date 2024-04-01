#Qs.........Move all negative elements to one side of array
#arr=[2,-3,4,5,6,-7,8,9]
#so above array shoud be -3,-7,4,5,6,2,8,9
arr=[2,-3,4,5,6,-7,8,9]
n=len(arr)
j=0
for i in range(0,n):
    if arr[i]<0:
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        j+=1
print(arr)

