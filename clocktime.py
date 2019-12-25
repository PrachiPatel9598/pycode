import time
def procedure():
	time.sleep(2.5)
#measure process time
t0=time.clock()
procedure()
print(time.clock()-t0,"seconds process time")
#measure wall time
t0=time.time()
procedure()
print(time.time()- t0,"seconds wall time")



#####output#######
'''C:\Users\prachi\Desktop\pythonfiles>python clocktime.py
clocktime.py:5: DeprecationWarning: time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8: use time.perf_counter or time.process_time instead
  t0=time.clock()
clocktime.py:7: DeprecationWarning: time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8: use time.perf_counter or time.process_time instead
  print(time.clock()-t0,"seconds process time")
2.5031959749999997 seconds process time
2.500039577484131 seconds wall time'''