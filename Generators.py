# Generators
# python generators are simple way of creating iterators.

# humain iteration to krni ha lakin memory full nhi bhrni to is liye iterator use hota ha.ye memory mein 1 1 store krta ha data ko.

# Python Generator: isky andar return statement nhi hoti. isky andar yeild statement hoti ha.

def gen_demo():
    
    yield "first statement"
    yield "second statement"
    yield "third statement"

gen = gen_demo()
print(next(gen))
print(next(gen))
print(next(gen))
# generator return mein ik generator object deta ha.


# yield vs return
# how they works
# generators mein ye hota ha ky jb ye variable ko call krta ha to usko yaad krta ha,ur next time next variable ko execute krta ha. jb ky normal function mein aisa nhi hota. normal func apna kaam khatam kr kay bhool jata ha lakin generator nhi bhoolta, yahi sb sy bara difference ha yield ur return mein.

# Example 2

def square(num):
    for i in range(1,num+1):
        yield i**2

gen = square(10)
print(next(gen))
print(next(gen))
print(next(gen))

for i in gen:
     print(i)
# ab dekho hua ye ha ky isny pehly next ky zariye 4 tk print kia ha,ur phir jb loop lagai to isny yaad rkha ky mene konsa pehly print kia tha ur wahin sy isny continue kia ha.


#   Range Function using generator

def mera_range(start,end):
    
    for i in range(start,end):
        yield i
        
gen = mera_range(15,26)
for i in gen:
    print(i)
    
    # isko hum aisay bhi likh skty han ky 

#for i in mera_range(15,26):
#    print(i)


# Generator Expression

# List Comprehension
L = [i**2 for i in range(1,101)]

# In generator,

gen = (i**2 for i in range(1,101))
for i in gen:
     print(i)   # it is known as Generator Expression
     

#   Practical Example
# In deep learning usage


# Benifits of Generators
#1. ease of use
#2. memory efficient
# 3. Representing infinite streams
#4. Chaining Generators

