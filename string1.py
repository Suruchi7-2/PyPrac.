#Strinng:immutable
#list:mutable also list can contain string,integer .can print any vakues by using inex.
#tuple:same as list but it is immutable.we need to write comma for tuple data type.and enclosed in paranthesis.
#iteraion can be on string list and tuple
#count method of sting can search for a partivcular substing and it will tell no. of occurence of that substring.
# we can use method center,ljust and rjust method of string to make string center,leftwards and rigtwards.
str="suruchi"
print(str.center(20," "))#20 tajkes maximum length of string including 
str="suruchi"
print(str.ljust(20,"-"))
str="suruchi"
print(str.rjust(20,"*"))
#isalpha returns true if all charactetr are albhabet
#isalnum returns true if all charcter are either number or either albhabet
#isspace returns true if all the  charcater in string are spaces
str1="suruchi"
str2="suru12"
str3=" "
print("String1 is",str1.isalpha())
print("String1 is",str1.isalnum())
print("String1 is",str1.isspace())
print()
print("String2 is",str2.isalpha())
print("String2 is",str2.isalnum())
print("String2 is",str2.isspace())
print()
print("String3 is",str3.isalpha())
print("String3 is",str3.isalnum())
print("String3 is",str3.isspace())
#join always worko with list and try to join sequence of charcter withother strings.
l=["suruchi","kumari"]
s=" "
print(s.join(l))

#find: find method of string try to find first cocourence of substring .takes paarameter,substring to be searched, then start index and last index.\
#rfind:this method try to find substring from rightside means always find substring last occurence in string.
str="this is a python tutorial"
print("first occurence is at, ",str.find("is"))
print("last occurence of substring is at, ",str.rfind("tut"))
#........
str="suruchi thakur"
str1="thakur"
str2="suruchi"
#startswith() function will always have a substring for which it will search in a string whether it is started with that substring if, it return true else fakse
#endswith()
print("is string started with suruchi: ",str.startswith(str2))
print("is string ended with thakur: ",str.endswith(str2))

#........
#isupper(): check whther in upper if,return True
#islower():check whether in lowercase,if ,returnn true.
str="suruchi"
s="SURU"
print("Check wheter s is in uppercase: ",s.isupper())
print("Check wheter str is in lowercase: ",str.islower())
#......
#isupper(): check whther in upper if,return True
#islower():check whether in lowercase,if ,returnn true.
str="suruchi is a good girl,she already succedin her life"
s="SURU"
print("Check wheter s is in uppercase: ",s.isupper())
print("Check wheter str is in lowercase: ",str.islower())
print("converted s into title case",str.title())#title method alwats capitize each start letter of each word.
print("converted s into upper case",str.upper())
print("converted s into lower case",str.lower())
print("converted s into swap case",str.swapcase())
print("converted s into swap case",str.swapcase())# swapcase always convert uppercase into lowercase vive versa.
#.................
#strip (),lstrip(),rstrip(): these methods removes leading and trailing character mentioned in its function arguments.
#using strip() to delete all "-"
str="........suruchhikumari........."
str2="abcdez"
print("remove all - available in string: ",str.strip('.'))
print("remove all - available from leftsidestring: ",str.lstrip('.'))
print("remove all - available from rightsidestring: ",str.rstrip('.'))
#min and max function can apploed to string to find smallest character and largest character
print("Smallest character: ",min(str2))
print("LArgetst charafcter: ",max(str2))
#.................
