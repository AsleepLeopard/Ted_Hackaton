# PROBLEM SET 1 - DONE
# Students will be asked to create an algorithm that can be used to calculate a number's factorial.
# The number should be entered by the user

number_to_process = int(input("\n Number to get factorail of: "))
multipliers = list(range(1, number_to_process + 1))
print(multipliers)
output_number = 1

for i in multipliers:
    output_number *= i 

print(f"{output_number}")

