proseString = """
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
"""

replacements = [
  ["An occupation", "OCCUPATION"],
  ["A country", "COUNTRY"],
  ["A plural noun", "PLURAL_NOUN"],
  ["A verb", "VERB"],
  ["An adjective", "ADJECTIVE"],
  ["A title that someone might have in an organization", "TITLE"],
  ["A personal item", "PERSONAL_ITEM"],
  ["A holiday", "HOLIDAY"],
  ["Your name", "NAME"]
]

for prompt, placeholder in replacements:
  userInput = input(prompt)
  proseString = proseString.replace(placeholder, userInput)

print(proseString)