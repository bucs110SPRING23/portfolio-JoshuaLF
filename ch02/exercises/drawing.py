import turtle

sides = int(input("How many sides are there?"))
length = int(input("What is the length of each side?"))

window = turtle.Screen()

tur = turtle.Turtle()
tur.shape("turtle")
tur.color("purple")
tur.speed(1)

internalAngle = 360/sides

for i in [0] * sides:
    tur.forward(length)
    tur.left(internalAngle)
    i = i + 1

'''
i = 0
while(sides > i):
    tur.forward(length)
    tur.left(internalAngle)
    i = i + 1
'''

window.exitonclick()