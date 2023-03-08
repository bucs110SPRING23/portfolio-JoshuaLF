import turtle

# simulate pen and paper
pen = turtle.Turtle()
pen2 = turtle.Turtle()
window = turtle.Screen()

pen.shape("turtle")
pen2.shape("turtle")

pen.color("purple")
pen2.color("orange")

pen.speed(1)
pen2.speed(0)
# variable = module.function()

pen.forward(100)
pen.left(50)
pen.forward(100)
pen.left(50)
pen.forward(100)
pen.left(50)
pen.forward(100)
pen.left(50)

pen2.fd(50) #fd is also forward
pen2.left(5)
pen2.up() #picks the pen up
pen2.fd(50)
pen2.left(5)
pen2.fd(50)
pen2.down() #puts pen down
pen2.fd(50)
pen2.left(5)
pen2.up
pen2.fd(50)
pen2.left(5)
pen2.fd(50)
pen2.down

colors = ["red" , "purple", "yellow", "green"]
for color in colors:
    pen.color(color)
    for _ in range(4):
        pen.left(90)
        pen.forward(50)
    pen.up()
    pen.forward(100)
    pen.down()

pen2.home() #goes home

pen.goto(0,0) #goes to points

# var = math.pi

# interface: what can I tell it to do, abstract away the details
# state: value of all its attributes
var = [1, 2, 3, 4, 5]
print(var)
var.append(6) #adds to end of list
print(var)

# ALWAYS must be the last turtle command (no more turtle commands after)
window.exitonclick()