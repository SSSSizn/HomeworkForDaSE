A = []
B = []
n = int(input("请输入数组元素个数"))
for i in range(n):
    A.append(i+1)  # 令数组A中的元素大小等于其数组角标加一
    B.append(1)  # 先为B数组进行初始化
for i in range(n):
    for k in range(i):
        B[i] = B[i] * A[k]
    for k in range(i+1, n):
        B[i] = B[i] * A[k]
print(B)
