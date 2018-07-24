n= int(input("nhap so n="))
print(n)

from turtle import *


speed(-1)
shape("turtle")
color("green")

for i in range(n):
    forward(100)
    left(360/n)


mainloop()