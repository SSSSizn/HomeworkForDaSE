# 因为2001 mod 3 = 0 2001 = 3 * 667，所以乘积最大的数组是由667个3组成的
import sys

# 若n = 1、2，则其最大正整数列就是本身
# 若n mod 3 = 0，则3 * m1 = n，可以将n划分为m1个3的数组，其乘积最大
# 若n mod 3 = 1，则3 * m2 + 1 = n，可以将n划分为由（m2-1）个3和两个2组成的数组，其乘积最大
# 若n mod 3 = 2，则3 * m3 + 2 = n，可以将n划分为由m3个3和一个1组成的数组，其乘积最大

n = int(input())
if n < 1:
    sys.exit(0)
result = [0]
if n < 2:
    result = [n]
elif n % 3 == 0:
    result = [3] * (n // 3)
elif n % 3 == 1:
    result = [3] * (n // 3 - 1) + [2, 2]
elif n % 3 == 2:
    result = [3] * (n // 3) + [2]
print("乘积最大的数列为", result)

