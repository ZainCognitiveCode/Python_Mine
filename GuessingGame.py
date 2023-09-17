# We have to run the game till it gets terminated
import random
random.randint(1,100)
print(random.randint(1,100))

jackpot=(random.randint(1,100))
guess=int(input("Guess it:"))
counter = 1
while guess !=jackpot:
    if guess<jackpot:
        print("Guess Higher")
    else:
        print("Guess Lower")
    guess=int(input("Guess it:"))
    counter+=1
    
print("Correct Answer")
print("You took",counter,"attempts")





