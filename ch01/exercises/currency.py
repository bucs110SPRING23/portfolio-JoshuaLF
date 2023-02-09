rate = input("What is the current exchange rate for the Euro to the Dollar?")
rate = float(rate) #casts it as a float instead of a string

amount = input("How much currency would you like to exchange?")
amount = float(amount)

total = amount * rate
result = total - 3

print(result)