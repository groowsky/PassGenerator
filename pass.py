import random

chars ='abcdefghijklmnoprstuwyqxzABCDEFGHIJKLMNOPRSTUWYQXZ-_=+[{]}\|,<.>/?!@#$%^&*()'
lenght = input('Password length? ')
lenght = int(lenght)
scale = input('How many passwords u need? ')
scale = int(scale)

for p in range(scale):
  password = ''
  for c in range(lenght):
      password += random.choice(chars)
  print(password)
