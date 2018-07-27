import turtle

vn = turtle.Screen()

turtle = turtle.Turtle()
turtle.speed(-1)

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

for n in range(3,8,1):    

        for i in range(n):
            turtle.color(colors[n-3])

            turtle.forward(100)
            turtle.left(360/n)
    


vn.mainloop()