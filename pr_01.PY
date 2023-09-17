# 1.User will input (3ages).Find the oldest one

# a = int(input("Enter first age:"))
# b = int(input("Enter Second age:"))
# c = int(input("Enter Third age:"))

# if(a>b and a>c):
#     print(f"The oldest one is{a} ")


# elif(b>a and b>c ):
#     print(f"The oldest one is {b}")

# else:
    
#     print(f"The oldest one is {c}" )
    
# 2.Write a program that will convert celsius value to fahrenheit

# Celsius = int(input("Enter the temperature value in celsius: "))
# fahrenheit = (Celsius* 9/5) +32
# print(f"The Temperature in {fahrenheit} is")


# 3.User will input (2numbers).Write a program to swap the numbers

# num1 = int(input("Enter 1st number"))
# num2 = int(input("Enter second number"))

# print("Original values:")
# print("Number 1:", num1)
# print("Number 2:", num2)

# num1 ,num2 = num2, num1

# print("\nAfter swapping:")
# print("Number 1:", num1)
# print("Number 2:", num2)


# 4.	Write a program that will give you the sum of 3 digits

# num1 = int(input("Enter 1st number:"))
# num2 = int(input("Enter second number:"))
# num3 = int(input("Enter Third number:"))
# sum = num1 + num2 +num3
# print(f"The sum of three number is {sum}")


# 5.Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

# user_input = int(input("Enter the number: "))
# num = user_input


# a = num %10
# # a = 3214 % 10 = 4: ye upar wali line ka code karay ga.
# num = num // 10
# # 3214//10 = 321: ye upar wali line ka code karay ga.
# b = num%10
# # 321%10 = 1: ye upar wali line ka code karay ga.
# num = num//10
# c = num%10
# d = num//10

# rev = 1000*a + 100*b +10*c +d
# print("Original Number: " ,user_input)
# print("reverse Number is : ", rev)

# if(user_input==rev):
#     print("True")
# else:
#     print("False")

# Second Method
# user_input = int(input("Enter the number: "))
# print(str(user_input)[::-1])


#6.	Write a program that will tell whether the number entered by the user is odd or even.

# num_entered = int(input("Enter the number "))
 
# if(num_entered%2==0):
#     print("The number is even")

# else:
#     print("The number is odd")


# 7.Write a program that will tell whether the given year is a leap year or not.

# def leapYear(year):
#     if(year%4==0 and year%100 !=0) or (year%4==0):
#         return True
#     else:
#         return False
    
# year = int(input("Enter the year"))
# if leapYear(year):
#     print("This is leap year")
# else:
#     print("This is not a leap year")

# 8.	Write a program to find the euclidean distance between two coordinates.

# import math 

# def euclidean_distance(x1,y1,x2,y2):
#     distance = math.sqrt((x2 - x1)**2 + (y2-y1)**2)
#     return distance

# x1 = float(input("Enter x-coordinate of the first point: "))
# y1 = float(input("Enter y-coordinate of the first point: "))
# x2 = float(input("Enter x-coordinate of the second point: "))
# y2 = float(input("Enter y-coordinate of the second point: "))


# d = euclidean_distance(x1,y1,x2,y2)
# print("The euclidean distance between two point is " , d)


# 9. Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.

# angle1 = float(input("Enter the first angle in degrees: "))
# angle2 = float(input("Enter the second angle in degrees: "))
# angle3 = float(input("Enter the third angle in degrees: "))

# if angle1 + angle2 + angle3 ==180:
#     print("This is a triangle")

# else:
#     print("This is not a triangle")


# 10.Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit

# costPrice = int(input("Enter the cost Price: "))
# SellingPrice = int(input("Enter the Selling Price: "))

# if (costPrice<SellingPrice):
#     print("This is the profit")

# else:
#     print("This is loss")

# 11.Write a program to find the simple interest when the value of principle,rate of interest and time period is given.
# p= int(input("Enter your principal: "))
# r= int(input("Enter your rate of interest: "))
# t = int(input("Enter your time period in years: "))
# i = (p*r*t)/100
# print("Your simple interest is: ", i)
# a = p + i
# print("Your amount is : ", a)


# 12.Write a program to find the volume of the cylinder. Also find the cost  ,when the cost of 1litre milk is 40Rs.
# r = float(input("Enter the radius: "))
# h = float(int(input("Enter the height: ")))
# v = 3.14*(r**2)*h
# print("Your volume is: ", v)
# cost = v/1000 * 40
# print("Your cost  is: ", "Rs.", cost)

# 13.Write  a program that will tell whether the given number is divisible by 3 & 6.

# num = int(input("Enter the number"))

# if(num%3==0 and num%6==0):
#     print("This number is divisible by 3 and 6")
# else:
#     print("This is not divisible by 3 and 6")

# 16.Write a program that will determine wheather when the value of temperature and humidity is provided by the user.
# TEMPERATURE(C)      HUMIDITY(%)      WEATHER

#       >= 30                             >=90                Hot and Humid
#       >= 30                             < 90                 Hot
#       <30                                >= 90               Cool and Humid
#       <30                                 <90                 Cool

# temp  = int(input("Enter the value of temperature: "))
# humidity  = int(input("Enter the value of Humidity: "))

# if(temp>=30 and humidity>=90):
#     print("The weather is Hot and Humid")
# elif(temp>=30 and humidity<90):
#     print("The weather is Hot")
# elif(temp<30 and humidity>=90):
#     print("The weather is Cool and Humid")
# elif(temp<30 and humidity<90):
#     print("The weather is Cool.")


# 17.Write a program that will take three digits from the user and add the square of each digit.

# d1 = int(input("Enter the first number:  "))
# d2 = int(input("Enter the Second number:  "))
# d3 = int(input("Enter the Third number:  "))
 
# square = d1**2 + d2**2 + d3**3
# print(square)

# 18.Write a program that will check whether the number is armstrong number or not.

#153
#  (1**3) + (5**3) + (3**3)
# user = int(input("Enter your number: "))
# num = user
# a = num%10
# num = num//10
# b = num%10
# c = num//10
# if(a**3) +(b**3) + (c**3)== user:
#     print("Armstrong Number")
# else:
#     print("Not an armstrong number")

# 19.Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not.
# user_input = int(input("Enter the four digit number: "))
# num = user_input
# a = num%10
# num = num //10
# b = num%10
# num = num//10 
# c = num%10
# d = num//10

# if (a**4) + (b**4) + (c**4) + (d**4) ==user_input:
#     print("Narcissitic Number")
# else:
#     print("Not a Narcissitic number")
# 20.Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20>= 30%)(0-1lakh print k).
# user_salary = int(input("Enter the annual salary: "))

# if user_salary>500000 and user_salary<1000000:
#     tax = (10/100)*user_salary
#     temp_salary = user_salary - tax
# elif user_salary>1100000 and user_salary<2000000:
#     tax = t(20/100)*user_salary
#     temp_salary = user_salary - tax
# elif user_salary>=2000000:
#     tax = (30/100)*user_salary
#     temp_salary = user_salary - tax

# print("After salary deduction ", temp_salary)

# HRA = (10/100) *temp_salary
# DA= (5/100)*temp_salary
# PF = (3/100)*temp_salary
# total_salary = (temp_salary-HRA-DA-PF)/12

# print("our in hand salary is: ", total_salary)

# if(total_salary<=999):
#     print(total_salary)
# elif total_salary>=1000 and total_salary<=9999:
#     print(total_salary/1000, "k")
# elif total_salary>=10000 and total_salary<=9999999:
#     print(total_salary/1000000, "l")
# else:
#     print(total_salary/10000000, "Cr")

    
# 21.Write a menu driven program 
# 1.cm to inches  
# 2.km to miles  
# 3.usd to inr  
# 4.exit

# user_input = int(input('''
# Hi! Welcome to my page.
# What would you like to do?
# 1. cm to inches
# 2. km to miles
# 3. usd to inr
# 4. exit'''))

# if user_input==1:
#     cm = float(input("Enter the cm: "))
#     inch = cm* 0.394
#     print("inches are: ", inch)
# elif user_input==2:
#     km = float(input("Enter the kkm: "))
#     miles = km*0.621
#     print(f"The miles in {km}km are: ", miles)
# elif user_input ==3:
#     usd = float(input("Enter the amount in USD: "))
#     inr = usd* 95
#     print(f"The amount of {usd}$ in inr is:  ", inr)

# else:
#     print("Exit")



# 22.Write a program that will tell the number of dogs and chicken are there when the user 
# will provide the value of total heads and legs.

# 23.Write a program that will swap numbers.
# a = int(input("Enter your first number:"))
# b = int(input("Enter your second number:"))

# a = a + b
# b = a - b
# a = a - b
# print("After swapping")
# print("Your a is :", a)
# print("Your b is :", b)

# 24.	Write a program to find the sum of first n numbers, where n will be provided by the user.
#  Eg if the user provides n=10 the output should be 55.

# n= int(input("Enter the number: "))
# sum = n*(n+1)/2
# print("Your sum is", sum)


# 25.	Write a program that can multiply 2 numbers provided by the user without using the * operator
# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# sum = 0

# for i in range(0,n1):
#     sum = sum + n2
# print("Your result is: ",sum)

# 26.	Write a program that can find the factorial of a given number provided by the user.

# num = int(input("Enter the number: "))
# i = 1
# if num>1:
#     while num>=1:
#         i = i*num
#         num = num -1
#     print("Your factorial is", i)

# else:
#     ("Your factorial is not possible")


# 27.	Write a program to print the first 25 odd numbers
# flag = 0
# i = 1

# while True:
#     if i%2 !=0:
#      print(i)
#     flag = flag+1
#     if flag==25:
#         break
#     i  = i + 1


# 28.	Write a program to print whether a given number is prime number or not.

# num = int(input("Enter your number: "))
# if num==2:
#     print("Prime number")
# elif num>1:
#     for i in range(2,num):
#         if(num%i)==0:
#             print(num, "is not a prime number")
#             break
#         else:
#             print(num, "is a prime number.")
#         break
#     else:
#         print(num,"is not a prime number.")

# 29.	Print all the armstrong numbers in the range of 100 to 1000

# for num in range (100,1000):
#     i = num
#     a = num%10
#     num = num//10
#     b = num%10
#     c = num//10

#     if(a**3) + (b**3) + (c**3)==i:
#         print(i)
#         i = i+1

# 30.	The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year. 
# You have to write a program to find out the population at the end of each of the last 10 years. For eg current population is 10000 so the output should be like this:
# 10th year - 10000
# 9th year - 9000
# 8th year - 8100 and so on

# flag = 0
# a = 10000
# print(a)

# while True:
#     b = (a) - ((10*a)/100)
#     a =b
#     print(int(b))
#     flag = flag+1

#     if flag==9:
#         break

# 31.Write a program to print all the unique combinations of 1,2,3 and 4.
# for i in range(1,5):
#     for j in range(1,5):
#         if(i != j):
#             print(i,j)

# 32.User will provide 2 numbers you have to find the HCF of those 2 numbers

# a = int(input("Enter the first number"))
# b = int(input("Enter the second number"))

# while a%b != 0:
#     rem = a%b
#     a = b
#     b = rem
#     print("Your HCF is", b)

# 33.	User will provide 2 numbers you have to find the by LCM of those 2 numbers.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# while a%b !=0:
#     rem = a%b
#     a = b
#     b = rem
# hcf = b

# lcm = (a*b)/hcf
# print("Your LCM is", lcm)

# 34.Print first 25 prime numbers.
# counter = 0
# num = 2  #2 is smallest prime number.
# while(counter<=25):
#     for i in range(2,num):
#         if num%i == 0:
#             break
#         else:
#            print(num)
#            counter = counter + 1
#         num = num + 1


# 35.Print the first 20 numbers of a Fibonacci series.
# count = 0
# a = 0
# b = 1
# print(a)
# print(b)

# while True:
#     c = a + b
#     a = b
#     b = c
#     print(c)
#     count = count + 1
#     if count==18:
#         break

# 37.Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# n = input("Enter the number")
# print("n is: ",n)
# nn = n + n
# print("nn is: ",nn)

# nnn =  n + n + n
# print("nnn is: ", nnn)

# c = int(n) + int(nn) + int(nnn)
# print(c)



# 38.	Take a number from the user and find the number of digits in it. 
# a = int(input("Enter your number: "))
# count = 0

# while(a>0):
#     a = a//10
#     count = count + 1
# print("number of digits: ", count)


# 39.	Print all factors of a given number provided by the user.

# num = int(input("Enter the number: "))

# for i in range(1,num+1):
#     if num%i ==0:
#         print("Your factor are: ", i)


# 40.Find the reverse of a number provided by the user(any number of digit) 

# a = int(input("Enter the number: "))
# rev = 0

# while a>0:
#     rem = a%10
#     a = a//10
#     rev = (rev*10) + (rem)
# print("Reversed values: ", rev)

# 41.	Write a program to print the following pattern
# *
# **
# ***
# ****
# *****

# row = int(input("Enter the number of rows: "))
# for i in range(0,row):
#     for j in range(0,row-i-1):
#         print(end= ' ')
#     for k in range(0,i+1):
#         print("*",end= ' ')
#     print()


# row = int(input('Enter the number of rows: '))

# for i in range(1,row+1):
#     for j in range(0,i):
#         print("#",end=' ')
#     print(' ')



# row = int(input('Enter the number of rows: '))

# for i in range(1,row+1):
#     for j in range(0,i):
#         print("#",end=' ')
#     print(' ')
# for k in range(row,0,-1):
#     for l in range(0,k-1):
#         print('#', end=' ')
#     print(' ')


# row = int(input("Enter the number of rows: "))

# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print(j,end = ' ')
#     for k in range(i-1,0, -1):
#         print(k,end = ' ')
#     print(' ')


# row = int(input("Enter the row value: "))
# num = 1
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print(num,end= ' ')
#         num = num + 1
#     print(' ')


# 46.	Write a program to calculate the sum of the following series till the nth term
# 1/1! + 2/2! + 3/3! + 4/4! +…….+ n/n!
# n will be provided by the user

# num = int(input("Enter your number: "))
# result = 0
# fact = 1 
# for i in range(1,num+1):
#     fact = fact * i
#     result = result + (i/fact)
# print(result)

# 47.Write a Python Program to Find the Sum of the Series till the nth term: 
# 1 + x^2/2 + x^3/3 + … x^n/n
# n will be provided by the user

# x = int(input("Enter your number: "))
# n = int(input("Enter nth value: "))
# sum = 1

# for i in range(2,n+1):
#     sum = sum+ ((x**i)/i)
# print(sum)

# 48. (x-1/x) + 1/2(x-1/x)**2 + 1/2(x-1/x)**3 +...+1/2(x-1/x)**7

# x = int(input("Enter the number: "))
# n = 7
# sum = ((x-1)/x)

# for i in range(2,n+1):
#     sum = sum + (1/2*((x-1)/x)**i)
# print(sum)

# 49.Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.

# num = int(input("Enter your number: "))
# add = 0
# avg = 0
# count = 0

# while True:
#     if num !=0:
#         add = add+num
#         count = count + 1
#         avg = add/count
#         num = int(input("Another number please: "))

#     else:
#         print("Thank You! ")
#         break

# print("Your sum is: ",add)
# print("Your avg is: ",avg)


# 50.	Write a program that accepts 2 numbers from the user a numerator and a denominator and then simplifies it
# Eg if the num = 5, den = 15 the answer should be ⅓
# Eg if the num = 6, den = 9 the answer should be ⅔

# a = int(input("Enter your first number: "))
# num1 = a
# b = int(input("Enter your second number: "))
# num2 = b

# while num1%num2 !=0:
#     rem = num1%num2
#     num1 = num2
#     num2 = rem
# hcf = num2

# a = a/hcf
# b = b/hcf
# print(a/b)


# 51.Find the length of a given string without using the len() function. 
# n = input("Enter the string: ")
# count = 0

# for i in n:
#     count = count+1
# print("length of the string is: ", count)

# 52.	Extract username from a given email. 
# Eg if the email is nitish24singh@gmail.com then the username should be nitish24singh

# email = input("Enter the email: ")
# username,mail = email.split('@') # ye @ sy phly walay ko username mein ur baki ko mail mein save kr day ga.
# print(username)


# 53.	Count the frequency of a particular character in a provided string.
#  Eg 'hello how are you' is the string, the frequency of h in this string is 2.

# a = input("Enter your string: ")
# b = input("Enter the character: ")
# count = 0 

# for i in a:
#     if i in b:
#         count = count+1
# print("Character occured",count,"times")

# 54.Find the index position of a particular character in another string.

# a = input("Enter the string: ") 
# b = input("Enter the character: ")
# print(a.index(b))

# 55.Count the number of vowels in a string provided by the user.

# a = input("Enter the string: ")
# vowels = "aeious"
# count = 0
# for i in a:
#    if i in vowels:
#     count = count+1
# print(count)

# 56.Write a program which can remove a particular character from a string. 
# a = input("Enter the string: ")
# b = int(input("Enter the value of the character: "))
# c = a[0:b-1] #mtlab 0 sy b tak,ur wahan 1 char remove kr do.
# d = a[b:]
# print(c+d)

# 57.Write a program that can check whether a given string is palindrome or not.

# a = input("Enter your string: ")
# rev = " "
# for i in range(len(a)-1,-1,-1):
#     rev = rev + a[i]
# print(rev)
# if rev==a:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# 58.Write a python program to remove all the duplicates from a list

# a = [1,2,3,3,4,6,7,7,8]
# b = []

# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

# 59.Write a python program to convert a string to title case without using the title()

# a = "hello vArTIKa sInGH"
# b = a.split()
# print(b)
# r = " "

# for i in b:
#     r = r+ i[0].upper() + i[1:].lower() + " "
# print(r)

# 60.Write a python program to find the max item from a list without using the max function

# l = [2,3,5,6,8,9]
# max = l[0]

# for i in l:
#     if i> max:
#         max = i
# print(max)

# 61.Write a python program to reverse a list.

# l = [1,2,3,4,5]
# rev = []

# for i in range(len(l)-1,-1,-1):
#     rev.append(l[i])
# print(rev)


# 62.Write a python program to search a given number from a list

# a = [1,2,3,4,5,7,8]
# num = int(input("Enter the number: "))

# for i in a:
#     if i == num:
#      print("True")
#      break

# else:
#     print("False")


# 63.Write a program that can create a new list from a given list where each item in the new list is square of the item of the old list.
 
# l = [2,3,4,5,6]
# l2 = []

# for i in l:
#     l2.append(i**2)
# print(l2)

# 64.Write a program that can reverse words of a given string.

# a = input("Enter your string: ")
# x = a.split()
# rev = []

# for i in range(len(x)-1,-1,-1):
#     rev.append(x[i])

# y = ' '.join(rev)

# print(y)

# 65.Write a program that can count the number of words in a given string

# a= input("Enter your string: ")
# count = 0

# for i in a:
#     if i == " ":
#         count=count+1
# words = count+1
# print("Number of words in the string: ",words)

# 66.Write a program to check if a list is in ascending order or not. 

# l = [4,2,3,1,5,0]
# flag = 0

# for i in range(0,len(l)-1):
#     if l[i]>= l[i+1]:
#         flag = 1
#         break
# if flag==0:
#     print("Sorted")
# else:
#     print("Not sorted")

# 67.Create 2 lists from a given list where 1st list will contain all the odd numbers from the original list 
# and the 2nd one will contain all the even numbers. 

# l = [1,2,3,4,5,6,7,8,9,10,12,11,13,14,15,16,17,18,19,20] 
# even = []
# odd = []

# for i in l:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)

# print("List of even numbers:",even)
# print("List of odd numbers:",odd)

# 68.Write a program to merge 2 list without using the + operator

# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9,10]
# l = []

# for i in l1:
#     l.append(i)

# for j in l2:
#     l.append(j)

# print("all items in a single list", l)

# 69.Write a program to replace an item with a different item if found in the list . 

# l = [1,2,3,4,5]
# find = int(input("Enter the number you want to replace: "))
# replace = int(input("Enter your number: "))

# for i in range(0,len(l)):
#     if find== l[i]:
#         l[i] =replace
#         print(l)
#         break
# else:
#     print("Not found")

# 70.Write a program that can convert a 2D list to 1D list. Write a program that can print. 

# L = [1,2,3,4,[5,7,8,]]
# rev = []

# for i in L:
#     if type(i)== list:
#         rev.extend(i)
#     else:
#         rev.append(i)
# print(rev)


# 71.Write a program that can perform union and intersection on 2 given list. 

# l1 = [1,2,3,4,5,6,7]
# l2 = [2,3,4,5,6,7,8,9,10,11]
# union = []
# intersec = []

# for i in l1:
#     if i not in union:
#         union.append(i)
# for j in l2:
#     if j not in union:
#         union.append(j)


# for i in l1:
#     if i in l2:
#         intersec.append(i)
# print("Union: ",union)
# print("Intersection: ", intersec)

# 72.the max item of each row of a matrix. 

# matrix = [
#     [1,2,3],[4,5,6],[7,8,9]
# ]

# for i in matrix:
#     max = i[0]
#     for j in i:
#        if j >max:
#         max = j
#     print(max)

# 73.Write a program that can convert an integer to string. 


# 74.Write a program to print the shape of a matrix. 
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# row = 0

# for i in matrix:
#     row = row+1
# print("The shape of this matrix is: ",row, "*", len(i))


# 75.Write a program that can check if you can perform matrix multiplication on 2 matrices. 

# matrix_1 = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# row_1 = 0
# for i in matrix_1:
#     row_1 = row_1+1
#     column_1 = len(i)
#     print("Matrix_1: ",i)
# print("Row_1: ", row_1)
# print("Column_1: ", column_1)



# matrix_2 = [
#     [2,3],
#     [4,5],
#     [6,7]
# ]

# row_2 = 0
# for j in matrix_2:
#     row_2 = row_2+1
#     column_2 = len(j)
#     print("Matrix_2: ",j)
# print("Row_2:", row_2)
# print("Column_2", column_2)

# if column_1 == row_2:
#     print("Multiplication is possible")
# else:
#     print("Multiplication is not possible")


# 76.Write a program to perform matrix multiplication on 2 matrices. 


# 77.Write a program that can sort a given unsorted list. Dont use any built in function for sorting.

# l = [5,2,3,6,4,7]

# for i in range (len(l)):
#     for k in range(0,len(l)-1):
#         if l[k]> l[k+1]:
#             temp = l[k]
#             l[k] = l[k+1]
#             l[k+1] = temp
# print(l)



# 84.Write a function that accepts a list of strings and performs Bag of words and convert it to numerical vectors.

# def bow(sentences):
#     vocab = []

#     for i in sentences:
#         vocab.extend(i.split())

#     vocab = list(set(vocab))

#     vector2d = []
#     for sentence in sentences:
#         vector = []

#         for word in vocab:
#             vector.append(sentence.count(word))
#         vector2d.append(vector)
#     return vector2d

# sentences = [
#     "Hello how are you?",
#     "I was waiting for your call",
#     "Where do you work?",
#     "Lets meet someday",
#     "Hope you are fine"

# ]

# a = bow(sentences)
# print(a)


# def nearest_neighbour(neighbours,you):
#     def calculate_distance(c1,c2):
#         return((c1[0]-c2[0])**2 + (c1[0]-c2[0])**2)**0.5
    
#     distances = []

#     for i in neighbours:
#         distances.append(calculate_distance(you,i))

#     neighbour_index,distance = sorted(list(enumerate(distances)),key = lambda x:x[1])[0]

#     print("Nearest neighbour is: ", neighbour_index,"at the distance of", distance)


# neighbours = [
#     [89,34],
#     [12,35],
#     [10,89],
#     [90,90]
# ]

# you = [-9.7]

# nearest_neighbour(neighbours,you)


# 83.Write a function that accepts a string and returns the number of upper case chars and lower case chars as a dictionary

# a = input("Enter your string: ")
# d = {}

# upper_count = 0
# lower_count = 0

# for i in a:
#     if (i.isupper()):
#         upper_count = upper_count+1

#     elif (i.islower()):
#         lower_count = lower_count + 1
    
# d = { "Upper case ": upper_count, "Lower case": lower_count}

# print(d)



# 79.	Assume a list with numbers from 1 to 10 and then convert it into a dictionary where the key would
#  be the numbers of the list and the values would be the square of those number. 

# l = [1,2,3,4,5,6,7,8,9,10]
# d = {}

# for i in l:
#     d[i] = i**2

# print(d)


# 78.Write a program that can find the most used word in a bollywood song

# a = '''
#  armadillo!
#  armadillo!
#  Where are you?

#  armadillo!
#  '''

# d = {}

# for word in a.split():
#     if word in d:
#         d[word] = d[word] + 1
#     else:
#         d[word] = 1

# max_val = max(d.values())

# for i in d:
#     if d[i] == max_val:
#         print(i,max_val)
#         break


# 80.Write a program to merge two given dictionary
# d1 = {'a':2, 'b':3}
# d2 = {'c':4, 'd':5}

# d = {}

# for i in d1:
#     d[i] =d1[i]
# for j in d2:
#     d[j] = d2[j]

# print(d)


# 81.	Write a program to swap the key value pair for max and min values
# Eg if the dict is like this {‘a’:1,’b’:2,’c’:3}
# Output should be {a:3,b:2,c:1}

# d = {'a':100, 'b':200, 'c':300, 'd':400}

# max_val = max(d.values())
# min_val = min(d.values())

# for i in d:
#     if d[i]==max_val:
#         print(d[i])
#     break

# for j in d:
#     if d[j] == min_val:
#         print(d[j])
#         break

# d[i] = min_val
# d[j] = max_val
# print(d)



# 85.Write a dummy program that can perform login and registration using a menu driven program. 

# database = {}

# def user_menu():

#     user_input = input(''' 
#         1. Enter 1 to register
#         2. Enter 2 to login 
#         3. Enter 3 to exit
#         ''')

#     if user_input == '1':
#             register()
#     elif user_input == '2':
#             login()
#     else:
#             print("Bye")

# def register():
#     name = input("Enter your name: ")
#     email = input("Enter your email: ")
#     password = input("Enter your password: ")

#     database[email]=[name,password]
#     print("Registration Successful")
#     print()
#     user_menu()


# def login():
#     email = input("Enter your email: ")
#     password = input("Enter your password: ")
#     flag = 0

#     for i in database:
#         if email == i:
#             flag = 1
#         if password == database[i][1]:
#             print("Welcome")
#         else:
#                 print("Incorrect credentials")
#     if flag == 0:
#         print("Email not found")

# user_menu()


# 73.Write a program that can convert an integer to string. 

# def convert(number):
#     digits = '0123456789'
#     result = ''
    
#     while number !=0:
#         current_num = number %10
#         result = digits[current_num] + result
#         number = number//10

#     return result

# print(type(convert(23)))


# 87.Write a function that accepts a number and returns it’s factorial. You can not use any loop

def fact(number):
    if number == 1:
        return 1
    else:
        return number*fact(number-1)

print(fact(6))



         


















    






        


    


        
























