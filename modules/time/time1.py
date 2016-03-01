__author__ = 'Tony'

import time

secs = time.time()
time_obj = time.struct_time(time.gmtime(secs))
year = time_obj.tm_year
month = time_obj.tm_mon
day = time_obj.tm_mday
hour = time_obj.tm_hour
minute = time_obj.tm_min
secs = time_obj.tm_sec

print (year, month, day, hour, minute, secs)
