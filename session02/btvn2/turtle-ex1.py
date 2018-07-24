import turtle

vn = turtle.Screen()

turtle = turtle.Turtle()
turtle.color("red","red")
turtle.speed(-1)

turtle.left(120)
for i in range(4):
    turtle.left(90)
    for i in range(2):
        turtle.forward(100)
        turtle.right(60)
        turtle.forward(100)
        turtle.right(120)


vn.mainloop()