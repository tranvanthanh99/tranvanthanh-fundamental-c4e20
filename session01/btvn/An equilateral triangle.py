import turtle

tn = turtle.Screen()

tamgiac = turtle.Turtle()
tamgiac.color("green","yellow")
tamgiac.fillcolor("yellow")

tamgiac.begin_fill()

for i in range(3):
    tamgiac.forward(100)
    tamgiac.left(120)

tamgiac.end_fill()


tn.mainloop()