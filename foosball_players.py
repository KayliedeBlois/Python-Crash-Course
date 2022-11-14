foosballers = [
  "Mia",
  "Retta",
  "Augustine",
  "Jin",
  "Waylon",
  "Alphonso",
  "Sage",
  "Hubert",
  "Raymon",
  "Rebecca",
  "Monty",
  "Glen",
  "Christi",
  "Patrice",
  "Craig",
  "Dexter",
  "Wally",
  "Ian",
  "Pat"
]

numberOfPlayers = len(foosballers)

#Get median player
median = numberOfPlayers//2
print(foosballers[median])

#Get the 5 players in the middle
print(foosballers[median - 2:median + 3])

#Add a player to the exact middle of the list
foosballers.insert(median, "Average Player")
print(foosballers)

#Change Average Player's name to AVERAGE PLAYER
foosballers[median] = "AVERAGE PLAYER"
print(foosballers)

#Add 5 new players
newPlayers = [
  "Ryan",
  "Kaylie",
  "Theo",
  "Cali",
  "Milo"
]

foosballers = foosballers + newPlayers
print(foosballers)

#Move "AVERAGE PLAYER to middle"
numberOfPlayers = len(foosballers)
newMedian = numberOfPlayers//2
del foosballers[median]
foosballers.insert(newMedian, "AVERAGE PLAYER")
print(foosballers)

#5 more ranked players show up, insert them into the appropriate location
foosballers.insert(7, "Lacy") #one spot ahead of Hubert
foosballers.insert(11, "Omar") #one spot behind Rebecca
foosballers.insert(7, "Otto") #8th best in the leqgue
foosballers.insert(-9, "Chauncey") #10 spots from the bottom
print(foosballers)