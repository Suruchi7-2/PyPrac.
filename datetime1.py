#Date and time module
#time() function
#returns time in seconds 
#ctime(): used to get current date and time.
#localtime(): it is used to convert seconds into date and time.returns an object struc_time and used to acces attribute using name.
from time import ctime,localtime,time
obj=localtime()
#print(obj)
print(obj.tm_hour)

e=ctime()
print(e)
#datetime odule have date and time. it has year, month,day,hour,minute,second,microsecond.
#if you need only date, use date class
#if u need time only use time class from datetime  module
from datetime import datetime
obj=datetime(year=2024, month=3 ,day=20, hour=15, minute= 36)
print(obj)
#now method calculate second of time and return
#today method of datetime clas, return day,hour,minute..
#month attribute
#year attribute
#hour attribute
from datetime import datetime
obj=datetime.today()
print(obj.day) 

#we can format date and time.
from datetime import datetime
obj=datetime.today()
new1=obj.strftime("%d-%m-%y")#strftime() function format today function into specif format.
print(new1)

#sleep method wait for speciified seconds.
import time
for i in range(15):
    if(i==9):
        time.sleep(2)
    print(i)

#calculate age using current date and dob.
from datetime import date
dob=date(2003, 4, 12)
obj=date.today()
age=obj.year-dob.year -((obj.month,obj.day)<(dob.month,dob.day))
print(age)
#comment