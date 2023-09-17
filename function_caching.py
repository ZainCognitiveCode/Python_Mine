# humaray pass kuch aisay functions hoty han jo kisi value ko chalany mein bht time letay han. hum isko function caching sy kam kr skty han time ko.
# mean ky agar humny pehly koi value calculate kr li ha to usko calculate krny ki dobara zaroorat nhi ha, balkay usko store kr lain takay time kam lagay.

import functools
import time

@functools.lru_cache(maxsize=None)
# is upar walin line ka mtlab ky hum lru_cache ko use kren gay functools sy ur maxsize dein gay ky itny tak wo store kr lay values ko.
def fx(n):
    time.sleep(5)
    return n*5

    
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

# isny sb sy phly wlay 6 ky bad train chala de,kyukny isny dobara compute nhi kia,balky cache sy utha kt use kia ha.
# ye cache aik program run mein maintain hoti ha
# memoization mein yahi ha ky jo result comoute ha usko dobara compute nhi krta.

