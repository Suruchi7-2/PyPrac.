#heap is much important for implementing priority queue ,for implementing heap sort for finding n smallest and n largest number
#heap is of two :min and max: in min, rood always less than or euqal to its children or leadf node.
import heapq
l=[5,7,9,2,4]
heapq.heapify(l)#heapify is used to convert list into heap.
print(list(l))#printing in list form 
#we can push new element into heap and heap will maintain its property automatically.
print(heapq.heappush(l,22),list(l))#it will push 22 into heap and maintain min heap property
print(heapq.heappop(l),",",list(l))#heapop will pop out root elemnt that will be smallest elemnt.
print(heapq.nlargest(2,l))#it will return 2 largest number from heap l
print(heapq.nsmallest(3,l))#itwill retun 3 smallest number from heap largest
#we have heappushpop function which works push and pop simultaneusly
#also we have heapreplace function
