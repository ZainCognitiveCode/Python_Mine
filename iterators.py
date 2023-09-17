# iteration
# iteration is a general term for taking each item of something, one after another. anytime,you use a loop,explicit or implicit,to go over a group of items, that is iteration.

# Example
#num = [1,2,3]

#for i in num:
    #print(i)

    
# iterator : iterator is an object that allows the programmer to traverse through a sequence of data without having to store the entire data in the memory.

# Example

L = [x for x in range(1,100000)]
#for i in L:
    #print(i*2)
    
import sys
print(sys.getsizeof(L)/24)

x = range(1,100000)
#for i in x:
     #print(i*2)
     
print(sys.getsizeof(x)/24)

# jb hum iterator ko use krty han to wo poray data ko memory mein load krta hi nhi ha,wo ik item ko load krta ha,ur wo execute hony ky baad agly ko karay ga.


# iterable
# iterable is an object which one can iterate over,jaisy upar list the.
# iterable generates an iterator when passed to iter() method.


# Example 
L =[1,2,3]
type(L)

# L is an iterable
#iter(L) --> iterator


# point to remember
# every iterator is also an iterable
# not all iterables are iterators

#   trick
#   Every iterable has an iter function
#   Eveery iterator has both iter function as well as a next function

a =2 
for i in a:
    print(i) # ye iterable nhi ha.
    
# ap dir function ko use kro,ur wahan a ko daal do, ur agar apko wahan iter dekhai de to wo iterable ban jaye ge.

# example 2 
T = (1,2,3)
print(dir(T))

t  = {1:2,3:4}
dir(t)


# ab ye dekhna ky koi iterator ha ya nhi
# agar dir chalany pr iter ur next function han to wo iterator ha.

L =[1,2,3]
dir(L)
# L is not an iterator

# hum iterable se iterator generate kr skty han

iter(L)
# ye mujy L ka iterator de ga.
# dir chalany pr pata chalay ga ky ye iterator bhi ha ur iterable bhi ha.


# UNDERSTANDING HOW LOOP WORKS

num = [1,2,3]

for i in num:
    print(i)

# sb sy phly humaray pass iterator hona chahhiye jis pr hum loop chala sakain.
# step1: loop sb sy iterator ko fetch krta ha
iter_num = iter(num)

# step 2 --> next function ko call krta ha.
# wo iterator ki state btata ha ky abhi hum kis item pr han, ky hum 0 pr han ya 1 pr
next(iter_num)  #output 1
next(iter_num)  #output 2
next(iter_num)  #output 3
next(iter_num)  #output: error ata ha  ky: stop iteration kyun ky 3 hi item hn humaray pass

# makin own loop
def mera_khudka_for_loop(iterable):
    
    iterator = iter(iterable)

    while True:
        
        try:
            print(next(iterator))
        except StopIteration:
            break
        
a = [1,2,3]
b = range(1,11)
c = (1,2,3)
d = {1,2,3}
e = {0:1,1:1}

mera_khudka_for_loop(a)

# A confusing point

num = [1,2,3]
iter_obj = iter(num)
print(id(iter_obj), "Address of iterator 1")
iter_obj2 = iter(iter_obj) #jb hum iterator pr iter chalain gy to wo phly wala iterator humain palat kr iterator de ga.
print(id(iter_obj), "Address of iterator 2")

# jb iterator pr iterator chalain gay to wo khud hi ho ga ur inka address same ho ga.

# iteration ka kaam:
# jb humain kisi object pr loop chalana ha to humain ye concept ana chahiye.


# create own range() function

class mera_range:   # koi bhi iterable hota ha usky andar iter magic method hona chahiye.
    def __init__(self,start,end):
        self.start = start
        self.end = end
        
    def __iter__(self):
        return mera_range_iterator(self)
    pass

class mera_range_iterator:
   
   def __init__(self,iterable_obj):
     self.iterable = iterable_obj
      
   
   def __iter__(self):
       return self
   
   def __next__(self):
       
       if self.iterable.start>= self.iterable.end:
           raise StopIteration
       current = self.iterable.start
       self.iterable.start += 1
       return current
   
for i in mera_range(1,11):
    print(i) 
    
# ye wahan use hoga deep learning mein.        



