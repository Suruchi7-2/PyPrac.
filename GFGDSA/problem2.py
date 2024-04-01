#you are given list of numbers ,obtained by rottaing a sorted list an unknowmn no of times.
#write function to determine minimum no of times original sorted list was rotatted to obtain given list
#time complexity should be o(log n).assume all number in list are unique
#example: list [5,6,9,0,2,3,4] was obtained by rotating sorted list [0,2,3,4,5,6,9] 3times
#means sorted list was rotated 3 times,then [5,6,9,0,2,3,4] found.
#we define rotating a list as removing last element of list and adding it before last element.
#sorted list refers as eleemnts are in increasing order.
#.................approach..........................
#if a sorted list rotated n times, then the smallest number of that list will be at position n.
#because rotating means adding last elemnt to first positon so, rotation 1 will add last element to first postion and hence smallest element of thata list will be at postion 1 starting from index 0.
#use linear search solution
#1.create variable psotion with value 0
#2.compare number at current positon to the number before it.
#3.if number is smaller than its predecessor,return positon
#4.otherwise incrrement positon and repaet till we exhaust all numbers.
