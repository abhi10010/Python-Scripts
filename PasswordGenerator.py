import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXWZ"
lowercase_letters = uppercase_letters.lower()
digits = "1234567890"
special_characters = ".,/?!@#$%&_=[]{}()"

all_characters = uppercase_letters + lowercase_letters + digits + special_characters

length = 16

password = "".join(random.sample(all_characters, length))

print(password)
