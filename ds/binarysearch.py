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
def binary_search(arr, target):
  low = 0
  high = len(arr) - 1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      high = mid-1
    else:
      low=mid+1
  return -1

# Example usage
arr = [13,11,10,7,4,3,2,1,0]
target = 2

result = binary_search(arr, target)

if result != -1:
  print(f"Element found at index: {result}")
else:
  print("Element not found in the array")



#Analyse time complexity for binary.
  #So. INitial length of array: N
  #on ist iteration: N/2
  #iteration 2: N/4
  #Iteration3:N/8 i.e. N/2^3
  #iteartion l:N/2^K
  #hence. final length of arrayis 1,we can calculate
  #N/2^k=1
  #N=2^K
  #k=log Nhence binary search runs in O(log N)log refers to log to the base 2.