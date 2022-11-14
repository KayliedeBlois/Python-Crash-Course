starburstColours = [
  "Pink", 
  "Red",
  "Orange",
  "Yellow"
]

# .append adds to end of the list
starburstColours.append("Blue")
print(starburstColours)

# .insert(index, item) inserts item to list
starburstColours.insert(1, "Green")
print(starburstColours)

# change value of index
starburstColours[0] = "More Blue"
print(starburstColours)

# del to delete index
del starburstColours[0]
print(starburstColours)

# concatenate lists to combine
moreColours = [
  "Purple",
  "Black"
]

starburstColours = starburstColours + moreColours
print(starburstColours)