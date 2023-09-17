import random

def check(comp, user):
    if(comp==user):
        return 0
    
    if(comp==0 and user==1):
        return -1
        

comp = (random.randint(0, 2))
user = int(input(" 0 for Snake, 1 for water and -1 for Gun"))


