questions = [[1,2], [3,5], [7,1], [1,4]]

score = 0

for a, b, in questions: 
  response = int(input("What's te value of " + str(a) + " + " + str(b) + "?"))
  if response == a + b:
    print("Correct!")
    score =+ 1
    print("Your current score is " + str(score) + "!")
  else: 
    print ("Incorrect")
    print("Your current score is " + str(score) + ".")

print("Your final score was " + str(score) + " out of " + str(len(questions)) + ".")