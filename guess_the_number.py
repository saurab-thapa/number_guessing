import random
guess=int(input("Guess a number between 1 and 100: "))
chance=4
orig_num=random.randint(1,100)
while(chance>1):
    if(guess==orig_num):
        print("Bingo!\nYou guessed it right...")
        break
    if(guess>orig_num):
        print("Too high!\nTry Again")
        print("Chances remaining : ",chance)
        guess=int(input("Guess again:"))
    if(guess<orig_num):
        print("Too low!\nTry Again")
        print("Chances remaining : ",chance)
        guess=int(input("Guess again:"))
    chance-=1

print("The number was :  ",orig_num)
