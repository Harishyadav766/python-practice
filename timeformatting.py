
from datetime import datetime           #time between two date-times
a = datetime(2016,10,6,0,0,0) 
b = datetime(2016,10,1,23,59,59)
print(a)
print(b)
print(a-b)
print((a-b).days)
print((a-b).total_seconds())


from datetime import datetime               #date time object tio the string
datetime_for_string = datetime(2016,10,1,0,0) 
datetime_string_format = '%b %d %Y, %H:%M:%S' 
a = datetime.strftime(datetime_for_string,datetime_string_format) 
print('a is :',a)

from datetime import datetime               #date string to datetime object 
datetime_string = 'Oct 1 2016, 00:00:00' 
datetime_string_format = '%b %d %Y, %H:%M:%S' 
b = datetime.strptime(datetime_string, datetime_string_format) 
print('b is :',b)