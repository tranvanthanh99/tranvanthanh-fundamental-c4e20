items=["T-Shirt","Sweater"]

n = input("Welcome to our shop, what do you want (C, R, U, D)? ").upper()


if n == "R":
    print("our items: ",end = "")
    print(*items,sep=", ")    
elif n == "C":
    create =input("Enter new item: ")
    items.append(create)
    print("our items: ",end = "")
    print(*items,sep=", ")
elif n== "U":
    position =input("Update position? ")      
    if position > len(items):
        print("index out of range")
    up =input("New item? ")
    items[position-1]=up
    print("our items: ",end = "")
    print(*items,sep=", ")
elif n =="D":
    delete= input("Delete position? ")   
    if delete > len(items):
        print("index out of range")
    del items[delete-1]
    print("our items: ",end = "")
    print(*items,sep=", ")




