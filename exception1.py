#IN python, also we have exception handling mechnaisam, since ,here is aldo run timeerror occurs hence this is needed
#we have standard run time exceptons like: Out of Index Error,Import Error,IO Error,ZeroDivision Error,TypeError
#Let'see try and except 
l=[2,3,4]
#print(l[3])
try:
    print("printing 1st elemnt: ",l[0])
    print("prinitng 4th elemnt: ",l[3])
except:
    print("not printed 4th element,error occured")
#so in above case, we can see we put our exception and hence no error came and our rest code is running while if exception will not be inside try,error found here index out of range
#now see mre exception
a=4 
#print("value of b= ",b)#throwing NammeError
try:
    b=a/0#this ZeroDivisonError
    print("value of b= ",b)
except(ZeroDivisionError, NameError):
    print("both error found")
#note: if exception not found in try block,then except would not running, if exception found,then only running
#now we have else block which will run when exception is not found in try block.see below
a=4 
#print("value of b= ",b)#throwing NammeError
try:
    b=a/1#no error found in try  blcok
    print("value of b= ",b)
except(ZeroDivisionError, NameError):
    print("both error found")#hence except will not run else run
else:
    print("b= ",b)
#in python, we can forcefully raise an error .
    #comment