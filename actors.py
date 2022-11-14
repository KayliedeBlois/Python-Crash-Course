actors = [
  "Nathan Fillion",
  "Gina Torres",
  "Alan Tudyk",
  "Morena Baccarin",
  "Adam Baldwin",
  "Jewel Staite",
  "Sean Maher",
  "Summer Glau",
  "Rob Glass"
]

roles = [
  "Captain Malcolm Reynolds",
  "Zoe Washburn",
  "Hoban Washburn",
  "Inara Serra",
  "Jayne Cobb",
  "Kaylee Frye",
  "Dr. Simon Tam",
  "River Tam",
  "Derrial Book"
]

creditReel = "Featuring:\n"

import time
for index, actor in enumerate(actors):
  #print(actor)
  #print(roles[index])
  creditReel = creditReel + actor + " as " + roles[index] + "\n"
print(creditReel)
