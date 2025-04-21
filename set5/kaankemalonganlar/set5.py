import random

array = ["a", "b" , "c" , "d", "e" "f", "g" ,"h" , "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "y", "z"]

domain = input("What's the domain? ")
mail = ""

for item in range(8):
    mail += random.choice(array)

print(mail+"@"+domain)
