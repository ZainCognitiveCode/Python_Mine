import time

# def usingWhite():
#     i = 0
#     while i<5000:
#         i = i+1
#         print(i)


# def usingFor():
#     for i in range(50000):
#         print(i)
        
# init = time.time()
# usingFor()
# t1= time.time() - init
# init = time.time()
# usingWhite()
# print(time.time() - init)
# print(t1)

# print(4)
# time.sleep(3)
# print("This is printed after 3 seconds")

# sleep sy wo hum diye gaye time tk sleep krwa skty han

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)

# time.strftime sy hum ye kr skty han ky humain is trha time chahiye to humain wo time usi format mein de ga.

