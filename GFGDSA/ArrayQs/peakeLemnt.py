"""Peak element
MediumAccuracy: 38.86%Submissions: 415K+Points: 4
Given an 0-indexed array of integers arr[] of size n, find its peak element. An element is considered to be peak if it's value is greater than or equal to the values of its adjacent elements (if they exist).

Note: The output will be 1 if the index returned by your function is correct; otherwise, it will be 0.

Example 1:

Input: 
n = 3
arr[] = {1, 2, 3}
Peak element's index: 2
Output: 
1
Explanation: 
If the index returned is 2, then the output printed will be 1. Since arr[2] = 3 is greater than its adjacent elements, and there is no element after it, we can consider it as a peak element. No other index satisfies the same property.
Example 2:

Input:
n = 7
arr[] = {1, 1, 1, 2, 1, 1, 1}
Output: 
1
Explanation: 
In this case there are 5 peak elements with indices as {0,1,3,5,6}. Returning any of them will give you correct answer.
Your Task:
You don't have to read input or print anything. Complete the function peakElement() which takes the array arr[] and its size n as input parameters and return the index of the peak element.

Expected Time Complexity: O( log(n) ).
Expected Auxiliary Space: O(1)
"""
"""SOlution...............................
in this qs, I had approch of linear traversing , but i got O(n compplexity), hence we have to move with another approach
let' see linear approach
1.agar n m bas ek element hai then index 0 return karo vohi peak hoga
2.agar array ka 1st elemnt o index >= index 0+1 se bada hoga then  return karo index 0
3.agar element n yaani index n-1 jiske right side eleemnt nahi h  vo apne n-2 elemnt se bada hoga then return index n-1
4.if now check for n=1 till n<n-1 in python ,for i in range(1,n-1)
5.check if a[i] >=a[i-1] and a[i]>=a[i+1]:
return index i 
6.repeat step 5 till loop run of step 4.
ab yehi index peak element hai chuki vo apne aaju baaju vale se bada hai
#...........APProach2 for o(logn BINSRY SEARCH)
just ismai humne ye dekhna h ki koi bhi index peak elemnt ka return kr denge apna kaam ban jaega
1.)so ,lo =0,high=n-1jab tak ye while loop chalega
find mid, and check if ,mid elemnt gretare than or equal to mid+1
agar mid hi bara hoga then just return high =mid
and agar nahi hoga bada then low intialise to mid+1 aur high us iteration , jo hoga vohi hoga like iteration 1st h then lo is 0 and high is 3 for 4 elemnt of array hence high abhi 3 h hoga for loop check karo
then 
#code"""
def peakElement(self, arr, n):
        low=0
        high=n-1
        while low<high:
            mid=low+(high-low)//2
            if arr[mid]>=arr[mid+1] :
                high=mid
            else:
                low=mid+1
        return high