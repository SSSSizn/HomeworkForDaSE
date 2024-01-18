arr = [i for i in input().split()]
length = len(arr)
for i in range(1, length):
    for j in range(i - 1, -1, -1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)
