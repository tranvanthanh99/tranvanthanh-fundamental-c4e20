bac = int(input("how many B bacterias are there? "))
time = int(input("how much time in minute will we wait? "))

for i in range(time//2):
    bac *=2
print("After",time,"minutes, we would have",bac,"bacterias")