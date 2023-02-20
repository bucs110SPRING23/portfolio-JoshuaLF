import random

randNum = int(random.randint(1, 10))

userG = 11

i = 0

while userG != randNum:
    userG = int(input("Guess the number between 1 and 10 (inclusive):"))

    if userG > randNum:
        print("Too high! Try again.")
    elif userG < randNum:
        print("Too low! Try again.")
    else:
        print("Correct!")
        break

    i += 1
    if i == 3:
        print("Too many tries. The number was:",randNum)
        break