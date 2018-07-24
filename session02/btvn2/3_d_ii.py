n= int(input("enter a number: "))
for row in range(1, n+1):
    for col in range(1,n+1):
        if (row + col) % 2 == 0:
            print('{:3}'.format(1), end="")
        else:
            print('{:3}'.format(0), end="")
    print()        
