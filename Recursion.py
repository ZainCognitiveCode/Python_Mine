# A function that call itself is called recursion.

# By iteration
def multiply(a,b):
    result = 0
    for i in range(b):
        result = result+a
    print(result)

print(multiply(3,4))

# By Recursion
def mul(a,b):
    if b==1:
        return a
    else:
        return a + mul(a,b-1)
    
print(mul(5,6))

# Factorial
def fact(number):
    if number==1:
        return 1
    else:
        # 5(factorial)=5*4!
        return number*fact(number-1)

print(fact(5))

# Palindrome
# A number or letter that remains the same even if the number and letters are inverted
# only one charcter or length is 1

def palin(text):
    if len(text)<=1:
        print("palindrome")
    else:
        if text[0]==text[-1]:
            palin(text[1:-1])
        else:
            print("Not a palin")
print(palin("madam"))
print(palin("malayalam"))
print(palin("python"))
print(palin("abba"))
        
# Rabbit Problem
import time
def fib(m):
    if m==0 or m==1:
        return 1
    else:
        return fib(m-1)+ fib(m-2)
    
start = time.time()
print(fib(36))
print(time.time()-start)










