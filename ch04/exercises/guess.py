import random

randNum = int(random.randint(1, 1000))

userG = 11

i = 0

while userG != randNum: #asks user to guess number
    userG = int(input("Guess the number between 1 and 1000 (inclusive):"))

    i += 1

    if userG > randNum:
        print("Too high! Try again.")
    elif userG < randNum:
        print("Too low! Try again.")
    else:
        print("Correct and it took you", i, "guesses!")
        break
        
compG = 500
binary = 250
tooLow = False
maxG = 1
while compG != randNum: #calculates number of binary search guesses
    if compG > randNum:
        tooLow = False
    else:
        tooLow = True

    if tooLow == True:
        compG += int(binary)
    else:
        compG -= int(binary)

    maxG += 1

    if compG == randNum:
        print("It would take a binary search algorithm",maxG, "guesses.")
        break
    elif binary == 1:
        pass
    else:
        binary = binary // 2
