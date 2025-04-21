array = [64, 56 , 78, 114, 22, 45, 1, 23, 54]
n = len(array)

for i in range(n - 1):
    for j in range(i + 1, n):
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]
print(array)