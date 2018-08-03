number = [1,6,8,1,2,1,5,6]
print("numbers = ",number)

num = input("Enter a number: ")

count = 0
for i in number:
    if i == num:
        count+=1

if count >1:
    print(num,"appers",count,"times in my list")
else:
    print(num,"appers",count,"time in my list")

