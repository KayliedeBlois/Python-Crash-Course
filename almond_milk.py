cartons = [
  ["Not almond milk", "Wrong logo"],
  ["Not almond milk", "Wrong logo"],
  ["Almond milk", "Wrong logo"],
  ["Almond milk", "Right logo"],
  ["Almond milk", "Wrong logo"]
]

cart = []

for carton in cartons:
  typeofMilk = carton[0]
  logo = carton[1]
  if typeofMilk == "Almond milk" and logo == "Right logo":
    cart.append(carton)
    break

if len(cart) == 0:
  cart.append("Beer")



#Using Else statement
cartons = [
  ["Not almond milk", "Wrong logo"],
  ["Not almond milk", "Wrong logo"],
  ["Almond milk", "Wrong logo"],
  ["Almond milk", "Right logo"],
  ["Almond milk", "Wrong logo"]
]

cart = []
wrongCartonsLookedAt = 0

for carton in cartons:
  typeofMilk = carton[0]
  logo = carton[1]
  if typeofMilk == "Almond milk" and logo == "Right logo":
    cart.append(carton)
    break
  else:
    wrongCartonsLookedAt += 1

if len(cart) == 0:
  cart.append("Beer")

print("I looked at " + str(wrongCartonsLookedAt) + " cartons that were not the right almond milk.")
