s = (input("What's the number? "))

firstdigit = (int(s[0]) + int(s[1])) % 10 
seconddigit = (int(s[1]) + int(s[2])) % 10
thirddigit = (int(s[2]) + int(s[3])) % 10

s = str(firstdigit) + str(seconddigit)+ str(thirddigit)

s = str(s)

fd = (int(s[0]) + int(s[1])) % 10 
sd = (int(s[1]) + int(s[2])) % 10 

if fd == sd:
    print("True")

else: 
    print("False")