# Multithreading is a technique that allows multiple threads of execution to run concurrently within a siingle process. In python, we can use the threading module to implement multithreading.

import threading
import time
from concurrent.futures import ThreadPoolExecutor

# indicate some task being done
def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)

def main():
# time1 = time.perf_counter()
# # Normal Code Execution    
# # func(4)
# # func(2)
# # func(1)
# time2 = time.perf_counter()
# print(time2 - time1)

 time1 = time.perf_counter()
# Same code using Threads
 t1 = threading.Thread(target = func,args=[8])
 t2 = threading.Thread(target = func,args=[10])
 t3 = threading.Thread(target = func,args=[11])

# ab yahan hum threading.thread ky zariye program ko run ky kabil banain gay, aur argument mein value pass kren gay. target mein function ka name likhain gay.

# ab hum python ko btain gy ky ye wala kaam start kr do takay sb kaam aik hi waqt mein ho sakain.
 t1.start()
 t2.start()
 t3.start()
# ye abhi start hua ha khatam nhi hua.


 t1.join()
 t2.join()
 t3.join()
# ye join ka mtlab ye ha ky jab tk t1 na khatam ho jye tb tk agla rukay ga execute hony ko ur jb saray khatam ho jain gy to execute ho jain gay.

# Calulating Time
 time2 = time.perf_counter()
 print(time2 -time1)

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(func,3)
        future2 = executor.submit(func,2)
        future3 = executor.submit(func,4)
        print(future1.result())
        print(future2.result())
        print(future3.result())
    
poolingDemo()

    

    