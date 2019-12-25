import datetime
#x=datetime.datetime(1998,6,26)
x=datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
print(x)
print(x.strftime("%a")) #abbreviated weekday name
print(x.strftime("%b")) #month name in short version
print(x.strftime("%B")) #month name in full version
print(x.strftime("%c")) #local version of date and time
print(x.strftime("%C")) #century number(the year divided by 100,range 00 -99)
print(x.strftime("%d")) #day of month 0-31
print(x.strftime("%D")) #same as %m/%d/%y
print(x.strftime("%e")) #day of the month(1 to 31)
print(x.strftime("%f")) #microsecond 00000-999999
print(x.strftime("%g")) #like %G,but without the century
print(x.strftime("%G")) #4-digit year corresponding to ISO week no.(see %V)
print(x.strftime("%h")) #same as %b
print(x.strftime("%H")) #hours 00-23
print(x.strftime("%I")) #hours 01-12
print(x.strftime("%j")) #day number of year 001-366
print(x.strftime("%m")) #month as a number 1-12
print(x.strftime("%M")) #minutes 00-59
print(x.strftime("%n")) #new character
print(x.strftime("%p")) #either AM/PM a/c to given time value
print(x.strftime("%r")) # time in am and pm notation
print(x.strftime("%R")) # time in 24 hour notation
print(x.strftime("%S")) #second 00-59
print(x.strftime("%t")) #tab character
print(x.strftime("%T")) #current time,equal to %H:%M:%S
print(x.strftime("%u")) #weekday as a number(1to7),monday=1
print(x.strftime("%U")) #week number of year sunday as first day of week 00-53
print(x.strftime("%V")) #hours 00-12
print(x.strftime("%w")) #weekdays as a number 0-6,0 is sunday
print(x.strftime("%W")) #week number of year monday as first day of week 00-53
print(x.strftime("%x")) #local version of date 
print(x.strftime("%X")) #local version of time
print(x.strftime("%y")) #year,short version,with century
print(x.strftime("%Y")) #year,full version
print(x.strftime("%z")) # UTC offset
print(x.strftime("%Z")) #Timezone
print(x.strftime("%%")) #A%character