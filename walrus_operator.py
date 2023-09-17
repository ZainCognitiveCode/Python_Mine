 # WALRUS OPERATOR
 # hum isky zariye value assign kr skty han variable ko within an expression.
 # iska symbol := ye ha
 
 # walrus  assigns values to variables as part of a larger expression
a = True
print(a:=False)

numbers = [1,2,3,4,5]
while (n:= len(numbers)) >0:
    print(numbers.pop())
    
# pop ka mtalb list mein akhri digit ko uthaye ga.

# is upar walay program mein humnay aik list banai ur phir while loop chalai ky jb tk n>0 h to number last sy first tk print ho,ur jb 0 aye to loop ruk jaye. humny walrus use kia to isliye humain n ko aledha print nhi krwana para.




#foods = list()
#while True:
#    food = input("What food do you like?: ")
#    if food == "quit":
#        break
             
#        foods.append(food)
        
foods = list()
while (food := input("What food do you like?: ")) != "quit":
     foods.append(food)       

 