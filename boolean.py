beatles = ["John", "Paul", "George", "Ringo"]
print(bool(beatles))
#True
print("Axl Rose" in beatles)
#False
print("John" in beatles)
#True

beatlesWhoHaveBeenToTheMoon = []
print(bool(beatlesWhoHaveBeenToTheMoon))
#False

shortSpeech = "I just wanted to thank everybody for everything."
print(bool(shortSpeech))
#True

speechless = ''
print(bool(speechless))
#False

linesofPythonWritten = 2688173
print(bool(linesofPythonWritten))
#True

timesAttackedByLions = 0
print(bool(timesAttackedByLions))
#False

isCoincidence = False
print(bool(isCoincidence))
#False

roomTemp = 23
plutoSurfaceTemp = -203
print(roomTemp<plutoSurfaceTemp)

#Compound Boolen Expressions
outsideTemp = 28
sunny = True
print(outsideTemp > 25 and sunny)
#True

print(outsideTemp > 28 and sunny)
#False

print(outsideTemp > 30 or sunny)
#True