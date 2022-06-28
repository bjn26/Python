print("Welcome to my computer quiz!!")
playing=input("Do you want to play? ")

if playing.lower()!="yes":
    quit()
print("Okay! Let's play:)")
score=0

ans=input("What does CPU stand for?")
if ans.lower()=="central processing unit":
    print("Correct!")
    score+=1

else:
    print("Incorrect!")

ans=input("What does ROM stand for?")
if ans.lower()=="read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans=input("What does RAM stand for?")
if ans.lower()=="random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans=input("What does GUI stand for?")
if ans.lower()=="graphical user interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans=input("What does IP stand for?")
if ans.lower()=="internet protocol":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) +" questions correct!")
print("You got "+str((score/5)*100)+"%.")

