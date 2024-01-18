def shell_sort(arr):
    n = len(arr)
    gap = int(n/2)
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = int(gap / 2)


array = [9, 87, 6, 54, 3, 21]
shell_sort(array)
print(array)
