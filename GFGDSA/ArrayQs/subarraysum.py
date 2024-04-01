"""Find Indexes of a subarray with given sum
MediumAccuracy: 16.5%Submissions: 1.5MPoints: 4
Given an unsorted array A of size N that contains only non negative integers, find a continuous sub-array that adds to a given number S and return the left and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.

Note:- You have to return an ArrayList consisting of two elements left and right. In case no such subarray exists return an array consisting of element -1.

Example 1:

Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.
Example 2:

Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements 
from 1st position to 5th position
is 15.
Your Task:
You don't need to read input or print anything. The task is to complete the function subarraySum() which takes arr, N, and S as input parameters and returns an ArrayList containing the starting and ending positions of the first such occurring subarray from the left where sum equals to S. The two indexes in the array should be according to 1-based indexing. If no such subarray is found, return an array consisting of only one element that is -1.

Expected Time Complexity: O(N)"""
#approach>>>..
"""tmhe, start index and end index find krni hai jiska sum given s ke equal ho
so tum ek loop i rkho jisse us sub array ki start track ho and j loop ko start kro jo j=i aur n tak chale inside i chalao 
and now sum varaible lo jisey 0 initliase kro,
and then sum+arr[j] issey array ka 1st elemnt 0 ke  saath add hoga aisey hi continuiosly add krte jao and check karo ki
tmhara sum s ke equal to nahi.agar h then i jo h vo hogi tmhari start index us subarray ki and j jo h abhi current vo hogi end index us subarray ki.

"""
def subArraySum(self,arr, n, s):
        l=[]
        found=False
        for i in range(n):
            sum=0
            for j in range(i,n):
                sum+=arr[j]
                if sum==s:
                    l.append(i+1)
                    l.append(j+1)
                    found=True
                    break
                #2nd Approach is sliding window ki concept use karo
"""tume two pointer concept lagao.
jo strat pointer hoga vo 0 hoga
end pointer 0 hoga
sum0 hoga
now loop par traverse from 0 till n:length of arr
sum=sum+a[i]
check if ur sum>=sum,if true then two condition will be sum may be eual ho s only ya greater ho
to jab only equal ho then bas end pointer yani last index of subarray jo h vo ab i ke eual hoga
and in case ur sum>s,and sstart<end,end abhi i ke equal ho chuka h then only
tmhe subtract krna h sum ko,ur sum-a[start]
and intialise start+=1
now again one loop jo check karega kya ab sum joh vo s ke equal h,if yes go insed if block
and just append ur current start into list l and also append current right into list l
remeber add one while appending start and end kuki 1based index h joki tmne 0based par kara h to start and end bhi 0 se tmhe de rhi
 isislie add 1 in both start and end."""
class Solution:
    def subArraySum(self,arr, n, s):
        l=[]
        left=0
        right=0
        isfound=False
        sum1=0
        for i in range(n):
            sum1+=arr[i]
            if sum1>=s:
                right=i
                while s<sum1 and left<right:
                    sum1-=arr[left]
                    left+=1
            if sum1==s:
                l.append(left+1)
                l.append(right+1)
                isfound=True
                break
        if not isfound:
            l.append(-1)
        return l