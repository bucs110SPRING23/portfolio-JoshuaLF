
def multiply(x, y):
    accumulator = 0
    for _ in range(y):
        accumulator += x
    return accumulator
    
def exponent(x, y):
    accumulator = 1 #needs to be one because of multiplication
    for _ in range(y):
        accumulator *= x
    return accumulator

def square(x):
    return multiply(x, x) #already wrote the code so why not use it

def main():
    x = int(input("Enter a number:"))
    y = int(input("Enter another number:"))
    print("\n")
    result = multiply(x, y)
    print(result)
    result = exponent(x, y)
    print(result)
    result = square(x)
    print(result)

main()