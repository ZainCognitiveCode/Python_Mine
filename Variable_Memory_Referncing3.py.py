L = [1,2,3]
print(id(L))

# nOW CHECK IT
print(id(1))
print(id(L[0]))

# 1 has id 3896,we will only use the last 4 digits
print(id(2))
print(id(L[1]))

# 2 has id 3928

print(id(3))
print(id(L[2]))

# 3 has id of 3960

# Python will store separately the addresses of each digit

L[2]=1
print(L)

# Now we have remove the reference of 3 and use 1 instead of it, so it will also point in the direction of first 1, so its value will be 3896

l1 = [1,2,3,[4,5]]




