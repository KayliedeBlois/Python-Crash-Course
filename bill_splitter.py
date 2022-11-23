print("What is your bill total?")
subtotal = input()

print("What percent tip do you want to give?")
tip = input()
tipAmount = subtotal * tip / 100


print("How many people are splitting the bill?")
people = input()

total = round(subtotal + tipAmount, 2)
pricePerPerson = round(total / people, 2)

print("Each person should pay:")
print(pricePerPerson)