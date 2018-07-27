menu=["death note","netflix","teaching"]
print("Hi there, here your favourite things so far")

print(20 * "* ")

for index, item in enumerate(menu):
     print("{}. {}".format(index +1,item))
print(20 * "* ")     

position=int(input("Position you want to update? "))
replace=input("your replacing favourite? ")
menu[position-1]=replace

print(20 * "* ")

for index, item in enumerate(menu):
     print("{}. {}".format(index +1,item))
print(20 * "* ") 