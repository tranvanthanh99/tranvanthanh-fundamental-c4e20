import turtle

wn = turtle.Screen()

vuong = turtle.Turtle()
vuong.color("green","yellow")
vuong.fillcolor("yellow")

vuong.begin_fill()

for i in range(4):
    vuong.forward(100)
    vuong.left(90)

vuong.end_fill()


wn.mainloop()



