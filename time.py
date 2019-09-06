from datetime import date
d1=date.today()
print(d1)
print(d1.month,d1.day,d1.year)
print(d1.weekday())

import datetime
dt = datetime.datetime.strptime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
print(dt)

from datetime import datetime, timedelta, timezone 
JST = timezone(timedelta(hours=+9))
dt = datetime(2015, 1, 1, 12, 0, 0, tzinfo=JST) 
print(dt)  


import datetime
today = datetime.date.today()
print('Today:', today)
yesterday = today - datetime.timedelta(days=1)
print('Yesterday:', yesterday)
tomorrow = today + datetime.timedelta(days=1) 
print('Tomorrow:', tomorrow)
print('Time between tomorrow and yesterday:', tomorrow - yesterday)

#import time
#from datetime import datetime
#from dateutil import tz
#utc = tz.tzutc()
#local = tz.tzlocal()

#print('utc:', utc)
#print('loacl:' ,local)
#utc_now = datetime.utcnow()
#print(utc_now)

import time
today = datetime.date.today()
print('today:', today)

yesterdy = today - datetime.timedelta(days=1)
print('yesterday:', yesterday)


import time
today = datetime.date.today()
print('today:', today)


yesterday = today - datetime.timedelta(days=1)
print('yesterday:', yesterday)


tomorrow = today + datetime.timedelta(days=1)
print('tomorrow:', tomorrow)

import time 
from datetime import datetime 
seconds_since_epoch=time.time()  #1469182681.709
utc_date=datetime.utcfromtimestamp(seconds_since_epoch) 
print('seconds_since_epoch:', seconds_since_epoch)
print('utc_date:', utc_date)


timestamp = time.time()
print('rimestamp:', timestamp)

localtimestamp = time.ctime(timestamp)
print('localtimestamp:', localtimestamp)

localtimestamp1 = datetime.fromtimestamp(timestamp)
print('localtimestamp1:', localtimestamp1)

localtimestamp1 = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
print('localtimestamp1:', localtimestamp1)


#import datetime
#from datautil.relativedelta import dateutil.relativedelta

#from dateutil.relativedelta import *
#d = datetime.datetime.strptime("2013-03-31", "%Y-%m-%d") 
#d2 = d - dateutil.relativedelta.relativedelta(months=1) 
#print(d2)

import calendar 
from datetime import date
def monthdelta(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12    
    if not m: m = 12    
    d = min(date.day, calendar.monthrange(y, m)[1])    
    return date.replace(day=d,month=m, year=y)
next_month = monthdelta(date.today(), 1) 
print('next_month:', next_month)

import calendar  
    
# using calender to print calendar of year  
# prints calendar of 2018  
print ("The calender of year 2018 is : ")  
print (calendar.calendar(2018, 2, 1, 6))  


import calendar
day = calendar.TextCalendar(calendar.SUNDAY)
calendar = day.formatmonth(2019,3)
print('calendar:',calendar)

import calendar
day = calendar.HTMLCalendar(calendar.SUNDAY)
calendar = day.formatmonth(2019,3)
print('calendar:',calendar)

import calendar
day = calendar.HTMLCalendar(calendar.MONDAY)
calendar = day.formatmonth(2019,1)
print('calendar:',calendar)



import calendar 
from datetime import date
for month in range(1, 13):
    mycal = calendar.monthcalendar(2025, month)
    week1 = mycal[0]
    week2 = mycal[1]
    if week1[calendar.MONDAY] != 0:
        auditday = week1[calendar.MONDAY]
    else:
        auditday = week2[calendar.MONDAY]
print ("%10s %2d" % (calendar.month_name[month], auditday))

import calendar
from datetime import date
day = calendar.firstweekday()
print('day:', day)

#import iso8601 
#iso8601.parse_date('2016-07-22 09:25:59') 


import time 
from datetime import datetime 
a= str(datetime.datetime(2016, 7, 22, 9, 25, 59, 555555)) 
print(a)

