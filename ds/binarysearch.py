#so, for binary search we have input numbers,ytarget numberand output whcih indicate position of target.
#inpput will be a list of numbers datastuctire
#target will be number which we need to find from list.
cards=[13,11,10,7,4,3,1]
query=7
output=3
def locate(cards,query):
    position=0
    while True:
        if(cards[position]==query):
            return position
        position+=1
        if(position==len(cards)):
            return -1
    
result=locate(cards,query)
print(result)
result==output
#time complxity is: O(N),space :O(1)
#here using linear search we can find output,like checking value from positiion 0 till length of list and in between if found query, return
#another for fast search we have binary
#but we can see,in above cards, we have sorted numbers in decreasing order, so we should utilise it and perform binary search
#.............steps for binary search.............
#1.Find middleelment of sorted list
#2.if it matches queried number return middle position as answer
#3.if it less than queried number ,then search frst half of list
#4.if it is greater than queried numebr theb search second half of list.
def locate(cards,query):
    lo=0 
    hi=len(cards)-1
    while(lo<=hi):
        mid=hi+lo//2
        if cards[mid]==query:
            print("Query found at mid: ",mid)
            return mid
        if cards[mid]<query:
            hi=mid-1
        if cards[mid]>query:
              lo=mid+1
    return -1
cards=[13,11,10,7,4,3,1]
query=13
result=locate(cards,query)
if result != -1:
    print("Element found at :",result)
else:
    print("ELement not found")



