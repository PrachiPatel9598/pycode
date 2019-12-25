import time
ticks=time.time()
print("Number of ticks since 12:00am,January 1,1970:",ticks)

#using localtime()
print(time.localtime())

#getting current time
localtime=time.localtime(time.time())
print("Loacal current time:",localtime)

# formatted time using asctime()
localtime=time.asctime(time.localtime(time.time()))
print("Local current time:",localtime)

t=time.localtime()
print("asctime:",time.asctime(t))

# #using altzone() for returning offset local DST timezone and in east of UTC 
# #(as in Western Europe,UK)
# import time
# print("time.altzone:",time.altzone()) //error

## ctime() converts a time expressed in seconds it is equivalent to asctime(localtime(secs))
print("ctime:" ,time.ctime())

##gmtime()

print("gmtime:",time.gmtime(1455508609.34375))

##mktime()
t=(2016,2,15,10,13,38,1,48,0)
d=time.mktime(t)
print("time.mktime(t): %f" % d)
print("asctime(localtime(secs)): %s" % time.asctime(time.localtime(d)))

#sleep()
print("Start: %s" % time.ctime())
time.sleep(5)
print("End: %s" % time.ctime())

#strftime()
##save as datetime.py

print("Tzset")

'''#tzset() resets the time conversion rules used by the library routines. The
environment variable TZ specifies how this is done
std offset [dst [offset [,start[/time], end[/time]]]]
'''

import os

os.environ['TZ']='EST+05EDT,M4.1.0,M10.5.0'
time.tzset()
print(time.strftime('%X %x %Z'))

os.environ['TZ']='AEST-10AEDT-11,M10.5.0,M3.5.0'
time.tzset()
print(time.strftime('%X %x %Z'))


