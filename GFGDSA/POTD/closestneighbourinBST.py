"""Given the root of a binary search tree and a number n, find the greatest number in the binary search tree that is less than or equal to n. 

Example 1 :

Input : 

n = 24
Output : 
21
Explanation : The greatest element in the tree which 
              is less than or equal to 24, is 21. 
              (Searching will be like 5->12->21)
Example 2 :

Input : 

n = 4
Output : 
3
Explanation : The greatest element in the tree which 
              is less than or equal to 4, is 3. 
              (Searching will be like 5->2->3)
Your task :
You don't need to read input or print anything. Your task is to complete the function findMaxForN() which takes the root of the BST, and the integer n as input parameters and returns the greatest element less than or equal to n in the given BST, Return -1 if no such element exists.

Expected Time Complexity: O(Height of the BST)
Expected Auxiliary Space: O(Height of the BST).
#...Question is simple
I have to find those elemnt which is less than or equal to n and will be gretaer element in treemeans n jo hoga vo greater or equal hoga us greatest elemnt se and vo greatest elemnt tree m bara hoga but n se less or eqaul hoga
#........APPPROACH
simple h 
1. pehle to greater elemnt ko none rkho then current m root daalo
2. then dekho jab tak current h loop chalao tab tmhe step 3 follow krni
3.loop true h then check if n>=current.data  means n jo h badi hagar current vallue se to filhal ke liey greater current ki value h and isiliye right move karo ab yaani current m current .right dalao
4agar if conditioin false h then ki n tmhara chhota h current se to tmhe definitely left traverse karni hogi kuki right m to current se bhi badi value hoogi and apna n jo h chhota h iisliye set current=current.left
and return ur greater.data.
"""
class Solution:
    def findMaxForN(self, root, n):
        greater=None
        current=root
        while current:
            if n>=current.key:
                greater=current
                current=current.right
            else:
                current=current.left
                
        return greater.key if greater else -1

