import random
import math

# 蒙特卡洛法
count = 0
for i in range(1000000):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    if x*x + y*y <= 1:
        count += 1
pi = count / 1000000 * 4
print(pi)

# 内接多边形

k = 6
a = 1
for i in range(14):
  k = 2 * k
  a = math.sqrt(2 - 2 * math.sqrt(1 - (a / 2) **2))
print(k * a / 2)

# 梅钦级数法
n = 10
t = n + 10
b = 10**t
p = b * 4 // 5
q = b // -239
s = p + q
n *= 2
for i in range(3, n, 2):
    p //= -25
    q //= -57121
    x = (p + q) // i
    s += x
pi = s * 4
pi //= 10 ** 10
pi /= 10 ** 10
print(pi)
