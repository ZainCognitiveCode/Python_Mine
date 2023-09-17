# Abstraction
# Decomposition
# means every component will connect together to make a decomposition

# Components of Function
# def is_even(i): def is identifier where is_even is the name of function, i is parameter or argument
# Then we will pass "" it. it is known as documentation string.it tells us that what is the purpose of our function and other information.
# Then comes the body of the function.
# x=i%2==0
# we get output by return x
# Call Function by is_even(7)

# Create a Function

def is_even(number):
    """
    This function tells if a given number is odd or even
    Input-any valid integer
    output-odd/even
    Created By-Zain
    Last edited-10 july 2023
    """
    if number%2 ==0:
        return "Even"
    else:
        return "Odd"

for i in range(1,11):
     print(is_even(i))
     
print(is_even.__doc__)
# it is used to print the documentation of a function.


# 2 point of views
# one who created function and one who use it.

import Zain as fd
fd.is_even("Hello")
print(fd.is_even("Hello"))

# Mene aik function banaya ur usko khud import krwaya aur aisa banaya kay ye crash na karay.

# Parameters Vs Arguments
# Jaisay aik games mein difficulty levels hotay han to difficulty level ko parameter kahain gay ur Arguments difficulties hon ge jaisay easy,medium and hard.


# 1. Default Argument
# 2. Positional Argument
# 3. Keyword Argument
# 4. Arbitrary Argument


# 1. Default Argument
def power(a,b):
    return a**b
print(power(2,3))
print(power(3,2)) 
# print(power(3)) #it will crash
# Solution is Default argument
def power(a=1,b=1): # ye bracket ky andar a=1 ka matlab yeh kay agar user 1 no. dalay ga to wo bhi return karay ge, kyunkay uski default value 1 ha
   return a**b
print(power(2,3))
print(power(2))
print(power())


# 2.Postional Argument
 # It means that if we send the value in the order than it will be written in the same order,just like we use (2,3) for (a,b)
 

# 3. Keyword Argument 
# Keyword argument has greater priority than Postional Argument. 
print(power(b=2,a=3))

# ye function 9 return karay ga kyunky key values de de gae han,ye is trha nhi karain ge kay b ki value pehly ko ml jaye ur a ki value dosry ko balkay jo keys han unko hi milay ge unki value.


# 4. Arbitrary Argument

def flexi(*number):
# (*number) ISKA MTLAB HA KAY NUMBERS KO TUPLE mein send krna ha humnay 
    product = 1
    print(number)
    print(type(number))
    for i in number:
        product= product*i
    print(product)
    
flexi(1)
flexi(1,2)
flexi(1,2,3,4,5,6,7)

# Benifits of Function
# Code Modularity
# Code Reusability
# Code Readability









    

