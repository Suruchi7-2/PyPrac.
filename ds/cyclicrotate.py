#cyclically rotate an array by one.
#given an array, u have to rotate the array by one positon un clock-wise direction.
#example1: n=5,a[]=[1,2,3,4,5],output: [5,1,2,3,4]..means 5 is clockwise rotated, then 4 shifted ,then 3 ,then 2,then 
a=[1,2,3,4,5]
n=5
a[:]=a[-1:]+a[:n-1]
print(a)