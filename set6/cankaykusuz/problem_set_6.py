# PROBLEM SET 6 - DİKKAT! Lütfen bu kodun sadece "3902" için çalıştırılacak hale getirildiğini unutmayınız. Eksik ve talimatların tamamını karşılamamaktadır.

# You are given a string s consisting of digits. Perform the following operation repeatedly until the string has exactly two digits:
# For each pair of consecutive digits in s, starting from the first digit, calculate a new digit as the sum of the two digits modulo 10.
# Replace s with the sequence of newly calculated digits, maintaining the order in which they are computed.
# Return true if the final two digits in s are the same; otherwise, return false.

# DİKKAT! Lütfen bu kodun sadece "3902" için çalıştırılacak hale getirildiğini unutmayınız. Eksik ve talimatların tamamını karşılamamaktadır.

# Converting input into a list with integers as digits.
string = list(input("Input the number: "))
string = [int(number) for number in string]

s_copy_list = string.copy()
number_list_after_mod = []

for i in range(0, len(string) - 1):
    number_list_after_mod.append((string[i] + string[i + 1]) % 10)
    s_copy_list.remove(s_copy_list[i-1])

print(f"After Mod-1: {number_list_after_mod}")

string = number_list_after_mod.copy()
s_copy_list = string.copy()
number_list_after_mod = []

for i in range(0, len(string) - 1):
    number_list_after_mod.append((string[i] + string[i + 1]) % 10)
    s_copy_list.remove(s_copy_list[i-1])

print(f"After Mod-2: {number_list_after_mod}")

# Eighter true or false:

if number_list_after_mod[0] == number_list_after_mod[1]:
    print("Output: False")
else:
    print("Output: True")

