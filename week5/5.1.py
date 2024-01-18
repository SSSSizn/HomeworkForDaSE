# 判断输入的a是否为质数
import sys

a = int(input())
b = 2
if a < 2:
    print(a, "不是质数")
    sys.exit()
if a == 2:
    print("2是质数")
    sys.exit()
while b < a:
    if a % b == 0:
        print(a, "不是质数")
        sys.exit()
    b += 1
print(a, "是质数")
