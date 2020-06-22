import random

def Generate_Ultimate_Password(length = 16):
  uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXWZ"
  lowercase_letters = uppercase_letters.lower()
  digits = "1234567890"
  special_characters = ".,/?!@#$%&_=[]{}()"   #Add or delete characters as per the given acceptance criteria

  all_characters = uppercase_letters + lowercase_letters + digits + special_characters

  sub_length = length//4

  password_uc = "".join(random.choices(uppercase_letters, k = sub_length)) #With Replacement
  password_lc = "".join(random.choices(lowercase_letters, k = sub_length)) #With Replacement
  password_d = "".join(random.choices(digits, k = sub_length)) #With Replacement
  password_sc = "".join(random.choices(special_characters, k = sub_length)) #With Replacement

  if length != sub_length*4:
    password_ac = "".join(random.choices(all_characters, k = length - (sub_length*4))) #With Replacement
  else:
    password_ac = ''

  password = "".join(random.sample(password_uc + password_lc + password_d + password_sc + password_ac, length)) #Without Replacement
  
  return password

print(Generate_Ultimate_Password(length = 15))
