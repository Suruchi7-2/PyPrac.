""" Problem statement
You are given an array 'A' of 'N' integers numbered from '0' to 'N - 1'.



You are required to find the number of elements 'A[i]' such that the median of 'A[i - 1]', 'A[i]' and 'A[i + 1]' is equal to 'A[i]'. You can consider 'A[i - 1]' for 'i' equal to '0' and 'A[i + 1]' for 'i' equal to 'N - 1' as '0'.

Example:
N = 3
A = [1, 3, 5]
The elements 'A[0]' and 'A[1]' satisfy the mentioned condition as the median of '0', 'A[0]' and 'A[1]' is 'A[0]', and the median of 'A[0]', 'A[1]' and 'A[2]' is 'A[1]'.
So, the answer for this case is '2'.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= 'N' <= 10^5
1 <= A[i] <= 10^5

Time limit: 1 sec
Sample input 1:
2
2
1 1
3
1 3 1
Sample output 1:
2
2
Explanation of sample input 1:
For test case 1:
The elements 'A[0]' and 'A[1]' satisfy the mentioned condition as the median of '0', 'A[0]' and 'A[1]' is 'A[0]', and the median of 'A[0]', 'A[1]' and '0' is 'A[1]'.
So, the answer for this case is '2'.


For test case 2:
The elements 'A[0]' and 'A[2]' satisfy the mentioned condition as the median of '0', 'A[0]' and 'A[1]' is 'A[0]', and the median of 'A[1]', 'A[2]' and '0' is 'A[2]'.
So, the answer for this case is '2'.
Sample input 2:
2
5
1 2 5 8 1
6
4 1 3 1 1 2
Sample output 2:
4
2
"""
#ou are given an array 'A' of 'N' integers numbered from '0' to 'N-1

#You are required to find the number of elements 'A[i]' such that the median of 'A[i-1]' ,'A[I]' and 'A[i + 1]' is equal to 'A[I]'. You can consider 'A[i-1]' for 'i' equal  to 0 and 'A[i + 1]' for 'i' equal to N - 1 as '0'.

#Example:

#N = 3 A = (1, 3, 5] The elements 'A[0]' and 'A[1]' satisfy the mentioned condition as the median of '0', 'A[0]' and 'A[1]' is 'A[0]', and the median of 'A[0]', 'A[1]' and 'A[2]' is 'A[1]. So, the answer for this case is '2'.
#Show drafts
def noofelement(n,arr):
    count=0
    answer=0
    for i in range(n):
        prev=0
        nextl=0
        curr=0
        if i>0:
            prev=arr[i-1]
        if i<n-1:
            nextl=arr[i+1]
        curr=arr[i]
        if (prev<=curr and curr<=nextl) or (prev>=curr and curr>=nextl):
            answer+=1
    return answer
n=3
arr=[2,3,5]
print(noofelement(n,arr))