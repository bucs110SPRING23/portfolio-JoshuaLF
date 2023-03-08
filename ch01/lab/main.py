import random

#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week = 4
print(classes_per_week, type(classes_per_week))
cost_per_class = cost_per_week/classes_per_week
print(cost_per_class, type(cost_per_class))
print("The class costs", cost_per_class, "per class for a week.")

#Part B
listStuff = ["turkey", "ham", "mustard", "cheese", "lettuce"] 
#I am a little hungry
randoChoice = random.choice(listStuff)
print(randoChoice)