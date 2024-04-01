"""Kth smallest element
MediumAccuracy: 35.17%Submissions: 570K+Points: 4
Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

Note :-  l and r denotes the starting and ending index of the array.

Example 1:

Input:
N = 6
arr[] = 7 10 4 3 20 15
K = 3
L=0 R=5

Output : 7
Explanation :
3rd smallest element in the given 
array is 7.
"""
#.................solution
class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        if len(arr)==1:
            return arr[0]
        arr.sort()
        return arr[k-1]
"""
so basically to find out kth smallest elemnt and kth largets elemnt
just sort it in ascendinfg ord descending order then find out its kth elemnt using index"""