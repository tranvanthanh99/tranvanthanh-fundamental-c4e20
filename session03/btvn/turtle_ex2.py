from turtle import *

speed(-1)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']

for n in range(5):
    color(colors[n])
    fillcolor(colors[n])
    begin_fill()
    
    for i in range(2):
        left(90)
        forward(100)
        left(90)
        forward(50)
        
    end_fill()    
    if n !=4:
        forward(50)    




mainloop()