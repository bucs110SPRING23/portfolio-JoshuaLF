import turtle
import random
from alphabet import *

window = turtle.Screen()
pen.shape("turtle") #doesn't work when I put into main

def main():
    name = input("Please input your first name:")
    name = name.upper()

    pen.penup()
    pen.goto(-300, 0)
    pen.pendown()

    for char in name:
        color = colors[random.randint(0, 4)]
        #color = randomColor()
        charOrd = str(ord(char))
        eval(charPrint[charOrd])
        moveOver()

    window.exitonclick()

# def randomColor(): #tried to pass this in but I could not get it to work
#     randomRed = int(random.randint(0, 255))
#     randomGreen = int(random.randint(0, 255))
#     randomBlue = int(random.randint(0, 255))
#     return (randomRed, randomGreen, randomBlue)

def moveOver():
    pen.penup()
    pen.forward(20)
    pen.pendown()

charPrint = {
    "65": "printA(color)",
    "66": "printB(color)",
    "67": "printC(color)",
    "68": "printD(color)",
    "69": "printE(color)",
    "70": "printF(color)",
    "71": "printG(color)",
    "72": "printH(color)",
    "73": "printI(color)",
    "74": "printJ(color)",
    "75": "printK(color)",
    "76": "printL(color)",
    "77": "printM(color)",
    "78": "printN(color)",
    "79": "printO(color)",
    "80": "printP(color)",
    "81": "printQ(color)",
    "82": "printR(color)",
    "83": "printS(color)",
    "84": "printT(color)",
    "85": "printU(color)",
    "86": "printV(color)",
    "87": "printW(color)",
    "88": "printX(color)",
    "89": "printY(color)",
    "90": "printZ(color)",
}

colors = ["black", "green", "blue", "red", "purple"]

main()