from random import *
x = randint(0, 100)
playing=True
count=0
print(x)
while playing:

    guess=int(input("Guess my number (0-100)? "))

    if guess > x:
        print("A little too large ;(")
    elif guess < x:
        print("too small :(")
    else:
        print("Bingo")
        break
    count+=1
    if count == 7:
        print("you lose")
        playing=  False   
