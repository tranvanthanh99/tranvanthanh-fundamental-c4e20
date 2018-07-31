name = input("your full name: ").lower()
a=name.split()


print("Updated:",end="  ")

for i in range(len(a)):
    b=list(a[i])
    b[0]=b[0].upper()
    c=''.join(b)
    print(c,end=" ")
    

