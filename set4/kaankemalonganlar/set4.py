array = [1,3,5,7]
array2 = [7,5,3,1]
boşluk = 0

for item in array2:
    print(" "*boşluk, "#"*item)
    boşluk = boşluk+1

array.pop(0)
boşluk = boşluk-1

for item2 in array:
    boşluk = boşluk-1
    print(" "*boşluk, "#"*item2)

    
