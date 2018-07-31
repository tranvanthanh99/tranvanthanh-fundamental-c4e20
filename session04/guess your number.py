

input("Now think of a number 0-100,then press 'ENTER'")
print("""
'c' if my guess is 'C'rrect
's' if my guess is 'S'maller than your number
'l' if my guess is 'L'arger than your number
""")


low=0
high=101

while True:

    mid = (low + high)  // 2

    guess=input("is {} your number".format(mid)).upper()

    if guess == "C":
            print("I knew it!!!!")
            break
    elif guess == "L":
        high=mid
    elif  guess =="S":
        low=mid  


