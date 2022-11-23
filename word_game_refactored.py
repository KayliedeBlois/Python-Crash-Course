letterHome = [
  # Title
  "A Letter Home",

# Prose string 
"""
Hi Mom, 

Just writing to tell you that I've quit my job as a OCCUPATION and I'm moving to
COUNTRY. The truth is, I've always been passionate about PLURAL_NOUN, and COUNTRY
is the best place in the world to build a career around them. I'll need to start 
small-- At first, all I'll be allowed to do is VERB near them, but when people 
see how ADJECTIVE I can be, I'm sure to rise to the top.

Don't worry about me, and tell dad to take good care of my PERSONAL_ITEM. I'll be
sure to call every HOLIDAY.

Love, 

NAME
""",

#Replacements 
  [
    ["An occupation: ", "OCCUPATION"],
    ["A country: ", "COUNTRY"],
    ["A plural noun: ", "PLURAL_NOUN"],
    ["A verb: ", "VERB"],
    ["An adjective: ", "ADJECTIVE"],
    ["A title that someone might have in an organization: ", "TITLE"],
    ["A personal item: ", "PERSONAL_ITEM"],
    ["A holiday: ", "HOLIDAY"],
    ["Your name: ", "NAME"]
  ]
]

sale = [

  # Title
  "A Great Sale",

  # Prose string
  """
  SALE SALE SALE
  
  Today only: Buy NUMBER PLURAL_NOUN and get a free NOUN!
  
  Sign up for our exlusive METAL card and receive 50% off your first purchase!
  """,

  # Replacements
  [
    ["A number", "NUMBER"],
    ["A plural noun", "PLURAL_NOUN"],
    ["A noun", "NOUN"],
    ["A type of metal", "METAL"]
  ]
]

showAndTell = [

  # Title
  "Show and Tell",

  # Prose string
  """Have you seen my pen ANIMAL? It's the best-- No pet can VERB1 as ADVERB as it can!
  It's NUMBER years old, and its name is NAME. You can VERB2 it if you want, but be careful, because it might VERB3.""",

  # Replacements
  [
    ["An animal", "ANIMAL"], 
    ["A verb", "VERB1"],
    ["An adverb", "ADVERB"], 
    ["A number", "NUMBER"], 
    ["A name", "NAME"], 
    ["A verb", "VERB2"], 
    ["A verb", "VERB3"]
  ]
]

stories = [
  letterHome, 
  sale, 
  showAndTell
]

selection = int(input("Choose a story"))
story = stories[selection]
print(story[0])
proseString = story[1]
replacements = story[2]

for prompt, placeholder in replacements:
  userInput = input(prompt)
  proseString = proseString.replace(placeholder, userInput)
print(proseString)