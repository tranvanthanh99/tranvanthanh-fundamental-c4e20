from turtle import *

speed(-1)
color("blue")
shapesize(0.1,0.1)
pensize(0.001)

right(135)


for n in range (1,61):
    for i in range (4):
        forward(120-2*n)
        right(90)    
    right(10)    




mainloop()
