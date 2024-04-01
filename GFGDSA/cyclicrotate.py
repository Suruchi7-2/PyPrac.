#cyclically rotate an array by one.
#given an array, u have to rotate the array by one positon un clock-wise direction.
#example1: n=5,a[]=[1,2,3,4,5],output: [5,1,2,3,4]..means 5 is clockwise rotated, then 4 shifted ,then 3 ,then 2,then 
a=[1,2,3,4,5]
n=5
a[:]=a[-1:]+a[:n-1]
print(a)
#print(a[-1:]) ya a[-1] dono hi 5dega but we need list isliye colon lagaya kuki 5 ke baad element ayenge

#Approach 2 ye hai ki humlog n-1 se element ko n pr shift kare then n-2 ko n-1 par and at index 0 -1 index ki value daale.
n = 8
a= [9, 8, 7, 6, 4, 2, 1, 3]
temp=a[-1]
for i in range(n-1,0,-1):
    a[i]=a[i-1]
a[0]=temp
print(a)#-1 , u have to write in range function so that it will go from reverse direction.