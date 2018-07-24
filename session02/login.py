import getpass

print("Hi there, this is superuser gateway")
user=input("Username: ")
if user == "c4e":
    pas=getpass.getpass("Passward: ")
    if pas == "codethechange":
        print("welcome")
    else:
        print("wrong")    
else:
    print("you`re not super user")    