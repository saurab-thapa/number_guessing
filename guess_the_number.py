import random
guess=int(input("Guess a number between 1 and 10: "))
chance=3
orig_num=random.randint(1,10)
while(chance>1):
    chance-=1
    if(guess==orig_num):
        print("Bingo!\nYou guessed it right...")
    else:
        print("Oops! Might need to try again")
        print("Chances remaining : ",chance)
        guess=int(input("Guess again:"))

print("The number was :  ",orig_num)
