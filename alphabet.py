for index, letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
  print(letter + " is the " + str(index + 1) + "th letter of the alphabet")

alphabet = "abcdefghijklmnopqrstuvwxyz"

vowelessAlphabet = alphabet
vowels = "aeiou"

for vowel in vowels:
  vowelessAlphabet = vowelessAlphabet.replace(vowel, "")

print(vowelessAlphabet)

favouriteAlphabet = alphabet
favouriteLetters = "qxrsy"

for letter in favouriteLetters:
  favouriteAlphabet = favouriteAlphabet.replace(letter, letter.upper())

print(favouriteAlphabet)