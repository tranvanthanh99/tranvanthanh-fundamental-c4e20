n=int(input("enter a number: "))

for j in range (1, n+1):
    for k in range(1, n+1):
        print("{:3}".format(j*k),end="")    
    print()    
