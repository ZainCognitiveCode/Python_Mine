sample ="how are you?"
# Split converts a list into string

print(sample.split())

L=[]

for i in sample.split():
    print(i.capitalize())
    L.append(i.capitalize())
    print(L)
    print(" ".join(L))
    
    # Now,by adding L We can get all the words in the string
    #We can capitalize every word by this method rather than doing a sinle word
    
    sample= "zain@gmail.com"
    print(sample[:sample.find("@")])
    
    

    

    
    


