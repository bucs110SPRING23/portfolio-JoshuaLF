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


""" or you could just use a for loop that says 'for i in range(3)'
that would stop it automatically after 3 instead of i += 1 """