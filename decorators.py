# Decorators
def greet(fx):
     def mfx():
         print("Good Morning")
         fx()
         print("Thanks for using this function")
     return mfx

#@greet     hum greet is trha bhi likh skty han
def hello():
    print("HELLO WORLD")

def add(a,b):
 print(a+b)

greet(hello)()      # ur is tha bhi likh skty han.



# hum chahty han ky humara jb function execute ho to sirf function execute na ho,balkay wo kuch karay bhi shi,mean good morning kahay phly ur function ky baad kuch ur kahay.