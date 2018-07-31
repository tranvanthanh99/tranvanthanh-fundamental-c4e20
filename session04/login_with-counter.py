print("Hi there, this is superuser gateway")
i=0

while True:


    users = input("Username: ")
    if users == "c4e":
        pas=input("Passward: ")
        if pas == "codethechange":
            print("welcome")
            break
        else:
            i+=1
            print("passwaord is incorrect")    
    else:
        i+=1
        print("username not exist")
    
    if i==3:
        print("you failed to log in 3 times, go away")
        break        