number = [1,6,8,1,2,1,5,6]
print("numbers = ",number)

num = int(input("Enter a number: "))

count = 0
for i in number:
    if i == num:
        count+=1

print(num,"appers",count,"time(s) in my list")