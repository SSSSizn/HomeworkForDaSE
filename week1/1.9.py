L = [1, 2, 3, 4, 5]
length = len(L)
K = [0] * length
M = [0] * length
count = len(L)
for i in range(1, count+1):
    K[i - 1] = L[count - i]
print(K)
p = count - 1
j = 0
while p > -1:
    M[j] = L[p]
    p -= 1
    j += 1
print(M)
