m = int(input())
tmp = m / 2
tmp1 = 0
tmp2 = m
while tmp*tmp*tmp != m:
    if tmp*tmp*tmp > m:
        tmp2 = tmp
        tmp = (tmp + tmp1)/2
    else:
        tmp1 = tmp
        tmp = (tmp + tmp2)/2
print(tmp)
    