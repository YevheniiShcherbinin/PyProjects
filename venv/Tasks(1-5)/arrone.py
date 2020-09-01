import random

arr = []
for i in range(1000):
    arr.append(random.randint(-1000, 1000))

avg = 0
summ = 0
for i in range(int(len(arr))):
    summ = summ + arr[i]
avg = summ / int(len(arr))
avgPluss = avg * 1.2
avgMinus = avg * 0.8

new_arr = []

for i in range(int(len(arr))):
    if arr[i] > avgPluss and arr[i] < avgMinus:
        new_arr.append(arr[i])

print(new_arr)
