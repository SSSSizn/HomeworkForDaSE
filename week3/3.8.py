import random
import time


def select_sort(arr):
    n = len(arr)
    for k in range(n - 1):
        mini = k
        for j in range(k + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[k], arr[mini] = arr[mini], arr[k]


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


a1 = [0]*500
a2 = [0]*1000
a3 = [0]*10000
for i in range(500):
    a1.append(int(random.uniform(1,10000)))
    a2.append(int(random.uniform(1, 10000)))
    a3.append(int(random.uniform(1, 10000)))
for i in range(500):
    a2.append(int(random.uniform(1, 10000)))
    a3.append(int(random.uniform(1, 10000)))
for i in range(9000):
    a3.append(int(random.uniform(1, 10000)))

start1 = time.time()
select_sort(a1)
end1 = time.time()
runtime1 = end1 - start1
start2 = time.time()
merge_sort(a1)
end2 = time.time()
runtime2 = end2 - start2
print("使用选择排序为长度为500的随机数组排序耗时", runtime1, "秒")
print("使用归并排序为长度为500的随机数组排序耗时", runtime2, "秒")

start1 = time.time()
select_sort(a2)
end1 = time.time()
runtime1 = end1 - start1
start2 = time.time()
merge_sort(a2)
end2 = time.time()
runtime2 = end2 - start2
print("使用选择排序为长度为1000的随机数组排序耗时", runtime1, "秒")
print("使用归并排序为长度为1000的随机数组排序耗时", runtime2, "秒")

start1 = time.time()
select_sort(a3)
end1 = time.time()
runtime1 = end1 - start1
start2 = time.time()
merge_sort(a3)
end2 = time.time()
runtime2 = end2 - start2
print("使用选择排序为长度为10000的随机数组排序耗时", runtime1, "秒")
print("使用归并排序为长度为10000的随机数组排序耗时", runtime2, "秒")
