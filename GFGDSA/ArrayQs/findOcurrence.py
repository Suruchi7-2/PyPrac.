"""Find the Frequency
EasyAccuracy: 77.19%Submissions: 70K+Points: 2
Given an Array Arr of N positive integers and an integer X. Return the frequency of X in the array.

 

Example 1:

Input:
N = 5
Arr = {1, 1, 1, 1, 1}
X = 1
Output: 
5
Explanation: Frequency of 1 is 5."""
def findFrequency (arr, n, x):
    return arr.count(x)