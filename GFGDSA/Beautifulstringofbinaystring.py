"""Problem statement
Ninja has been given a binary string ‘STR’ containing either ‘0’ or ‘1’. A binary string is called beautiful if it contains alternating 0s and 1s.

For Example:‘0101’, ‘1010’, ‘101’, ‘010’ are beautiful strings.

He wants to make ‘STR’ beautiful by performing some operations on it. In one operation, Ninja can convert ‘0’ into ‘1’ or vice versa.

Your task is to determine the minimum number of operations Ninja should perform to make ‘STR’ beautiful.

For Example :
Minimum operations to make ‘STR’ ‘0010’ beautiful is ‘1’. In one operation, we can convert ‘0’ at index ‘0’ (0-based indexing) to ‘1’. The ‘STR’ now becomes ‘1010’ which is a beautiful string. 
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= T <= 100
2 <= |STR| <= 10^5
STR[i] = ‘1’ or ‘0’

Where '|STR|' denotes the length of ‘STR’.

Time Limit: 1 sec 
Sample Input 1 :
2
0000
1010
Sample Output 1 :
2
0
Explanation of Sample Input 1 :
For the first test case:
The two beautiful strings that can be formed from the given ‘STR’ 
are “1010” and “0101”. Ninja can transform ‘STR’ to “1010” by 
performing the following operations:
Replace ‘0’ at index 0 by ‘1’.
Replace ‘0’ at index 2 by ‘1’.

Ninja can transform ‘STR’ to “0101” by performing the following 
operations:
Replace ‘0' at index 1 by ‘1’.
Replace ‘0’ at index 3 by ‘1’.

The minimum number of operations in transforming ‘STR’ to either of the two beautiful strings is 2.

For the second test case:
Given ‘STR’ is already beautiful so the minimum number of operations required is 0.
Sample Input 2 :
2
01011
1001
Sample Output 2 :
1
2
"""
def makeBeautiful(str):
	count1=0
	count2=0
	for i in range(len(str)):
		if i & 1:
			if(str[i]=='0'):
				count1+=1
			if(str[i]=='1'):
				count2+=1
		else:
			if(str[i]=='1'):
				count1+=1
			if(str[i]=='0'):
				count2+=1
	return min(count1,count2)
