import random

arr = []
for i in range(1000):
    arr.append(random.randint(-1000, 1000))
    max1 = max(arr)
    max2 = min(arr)
for n in arr:
    if n > max2 and n != max1:
        max2 = n
print(max1, max2)


# ind_max1 = arr.index(max1)
#max2 = 0
#if arr[i] > max1:
# max2 = max1
#max1 = arr[i]
#else:
#if arr[i] > max2:
# max2 = arr[i]
#print(max1, max2)


