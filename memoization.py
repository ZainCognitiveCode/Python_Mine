# By dynamic programming,we can reduce time. First store the calculated value and calculate the required value.
# We trade space and time in dynamic
import time
def memo(m,d):
    if m in d:
        return d[m]
    else:
        d[m]= memo(m-1,d)+memo(m-2,d)
        return d[m]
    
start = time.time()
d = {0:1,1:1}
print(memo(500,d))
print(time.time()-start)

