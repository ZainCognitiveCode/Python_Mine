# Kon Banay ga Core pati.
# Use list data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.

questions = [
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4], 
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4],    
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4],    
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4],    
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4],    
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4],    
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4]    
]

levels = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

for i in range(0,len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"a.{question[1]}        b.{question[2]}")
    print(f"c.{question[3]}        d.{question[4]}")
    reply = int(input("Enter your answer (1-4)"))
    if(reply== question[-1]):
        print(f"correct answer, you have won Rs.{levels[i]}")
        if(i==4):
            money =10000
        elif(i==9):
            money = 320000
        elif(i==14):
            money = 10000000
    else:
        print("Wrong answer!")
        break
    
print(f"Your take home money is {money}")
