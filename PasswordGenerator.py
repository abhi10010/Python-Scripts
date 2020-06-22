import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXWZ"
lowercase_letters = uppercase_letters.lower()
digits = "1234567890"
special_characters = ".,/?!@#$%&_=[]{}()"   #Add or delete characters as per the given acceptance criteria

all_characters = uppercase_letters + lowercase_letters + digits + special_characters

length = 16                                 #Change the length according to the requirement

sub_length = length//4

password_uc = "".join(random.sample(uppercase_letters, sub_length))
password_lc = "".join(random.sample(lowercase_letters, sub_length))
password_d = "".join(random.sample(digits, sub_length))
password_sc = "".join(random.sample(special_characters, sub_length))

if length != sub_length*4:
  password_ac = "".join(random.sample(all_characters, length - (sub_length*4)))
else:
  password_ac = ''

password = "".join(random.sample(password_uc + password_lc + password_d + password_sc + password_ac, length))

print(password)
