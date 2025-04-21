number = int(input("What's the number? "))

result = 1
for item in range(1,number+1):
    result = result*item

print(result)