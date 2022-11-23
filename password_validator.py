password = input("Create password: ")

passwordCheck = input("Input your password again to validate it: ")

if password == passwordCheck and len(password) >=  8:
  print("You've set your password!")
elif len(password) < 8:
  print("Passwords must be atleast 8 characters.")
else: 
  print("Your passwords do not match, try again,") 