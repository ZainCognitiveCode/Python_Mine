# function: as  you know that. 
# pure idempotent. //mean it does not change it behavior. 
# no global state 
# no change arguments 
# results -> arguments


# python follows procedural paradigm. just like recipe,what to do first and what to do last. specific instruction. global state. 


# Functional Programming 
# functions are first class value.  
# lambda calculus
# recursion



# Optimization
# tail recursion
# if result not needed, do not call a function. 
# 2 func. dont depend,parallel. 
# 2x same params, remember the result. 
# result memoization. 
# in line add(a,b)


# Lazy Evaluation 
# do not actually call the function,if you need the result than call it. 
# iterators is an example of lazy evaluation. 


#Lambda Calculus 
# lambda is an expression. it is a callable function. 
# lambda a,b: a+b 
# lambda *args: len(args)
# lambda x: x**3


#filter 
#filter(func,iterable) -> iterartor

#filter(lambda a:a%2==1,reversed (range(100))) -> iterator. 
# next(i) = 99
# next(i) = 97
# .... 


#map 
#map(func,iterables,...) -> iterator 
# map(lambd x:x**3,range(5)) -> iterator 
# next(i) = 0
#next(i) = 1
#next(i) = 8
# i = map(lambda x,y: x+y, range(10),range(10,20))
# next(i) = 10
# next(i) = 12


#zip
#zip(iterable,...) -> iterator
# i = zip(range(10),range(10,20),range(20,30))
# next(i) = (0,10,20)
# next(i) = (1,11,21)
#next(i) = (2,12,22)


#functools
#fuctools.partial(func,args...) -> function 
# import functools
# functools.partial(add, 3)(5) -> 8
# functools.reduce(func,iterable,initializer=Name)
# functools.reduce(add,(1,2,3),0) -> 6 
