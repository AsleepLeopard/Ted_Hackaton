array = [64, 56 , 78, 114, 22, 45, 1, 23, 54]

max1 = max(array)
min1 = min(array)

array.remove(max1)
array.remove(min1)

max2 = max(array)
min2 = min(array)

array.remove(max2)
array.remove(min2)

max3 = max(array)
min3 = min(array)

array.remove(max3)
array.remove(min3)

max4 = max(array)
min4 = min(array)

array.remove(max4)
array.remove(min4)

mid = array[0]

array2 = [min1, min2 ,min3, min4, mid, max4, max3, max2, max1]

print(array2)

