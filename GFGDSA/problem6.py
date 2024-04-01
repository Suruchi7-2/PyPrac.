#u have two array now find union f that
#Approach2
a=[1,3,2]
b=[4,2,6]
s=a.set(a)
s1=b.set(b)
s.union(s1)
print(s)
#Approach2
a=[1,3,2]
b=[4,2,6]
n=3
m=3
s=set()
for i in range(0,n):
    s.add(a[i])
for i in range(0,m):
    s.add(b[i])
    print(len(s))