import turtle

vn = turtle.Screen()

turtle = turtle.Turtle()
turtle.speed(-1)

   

for n in range(3,7,1):
    if n%2==0:
       turtle.color("red","red")
    else :
       turtle.color("blue","red")    

    for i in range(n):
        turtle.forward(100)
        turtle.left(360/n)

   

vn.mainloop()