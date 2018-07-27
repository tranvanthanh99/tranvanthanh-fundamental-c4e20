menu=["death note","netflix","teaching"]

print("Hi there, here your favourite things so far")
print(*menu, sep=", ")

a=input("name onething you want to add: ")
menu.append(a)

print(*menu, sep=", ")