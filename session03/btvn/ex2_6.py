size =[5, 7, 300 ,90, 24, 50, 75]
print(size,end = print("hello, my name is Thanh and here are my sheep sizes "))

big=max(size)
print("Now my biggest sheep has size",big,"Let`s sheer it")

index=size.index(big)
size[index]=8

n=0
total=0

while True:
    n+=1

    print("Month",n,":")
    for i in range(7):
        size[i]+=50
    print(size,end = print("One month has passed, now here is my flock "))
    if n ==3:
        for i in range(7):
            total += size[i]
        money=total*2
        print("My flock has size in total: ",total)
        print("I would get",total,"* 2$ =",money,end="$")    
        break

    big=max(size)
    print("Now my biggest sheep has size",big,"Let`s sheer it")

    index=size.index(big)
    size[index]=8
    print(size,end = print("After sheering, here is my flock "))
