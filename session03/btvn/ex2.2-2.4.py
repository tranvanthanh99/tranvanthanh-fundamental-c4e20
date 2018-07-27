size =[5, 7, 300 ,90, 24, 50, 75]
print(size,end = print("hello, my name is Thanh and here are my sheep sizes "))

big=max(size)
print("Now my biggest sheep has size",big,"Let`s sheer it")

index=size.index(big)
size[index]=8
print(size,end = print("After sheering, here is my flock "))

for i in range(7):
    size[i]+=50
print(size,end = print("One month has passed, now here is my flock "))


