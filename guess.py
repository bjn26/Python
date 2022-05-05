import random
num=random.randint(5,30)
print("Enter between 5 and 30")
for guesses in range(1,5):
    print("Enter guess:")
    guess = int(input())
    if(guess>num):
        print("Your guess is high.")
    elif(guess<num):
        print("Your guess is low.")
    else:
        break
if(guess==num):
 print("you guessed" +str(guess)+"is right")
else:
 print("your guess is wrong.Correct is " +str(num))
