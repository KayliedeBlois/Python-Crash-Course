instructionsSteps = [
  "turn left",
  "go straight for 2 blocks",
  "keep going until you see the dog statue",
  "turn right",
  "turn right again",
  "park right on the sidewalk"
]

instructions = "First, "

for nextInstruction in instructionsSteps:
  instructions = instructions + nextInstruction + ", then "

print(instructions + "you're there!")

#all uppercase
instructionStepsButScreamed = []

for nextInstruction in instructionsSteps:
  upperInstructions = nextInstruction.upper()
  instructionStepsButScreamed.append(upperInstructions)

print(instructionStepsButScreamed)