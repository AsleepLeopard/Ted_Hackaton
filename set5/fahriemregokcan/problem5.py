domain = input("Enter a domain:")
f = 8
t = ""
alfabe = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
          "u", "v", "w", "x", "y", "z"]
for x in range(f):
    r = random.randrange(27)
    t += alfabe[r]
print(t + "@" + domain)