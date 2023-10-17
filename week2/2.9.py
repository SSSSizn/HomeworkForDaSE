import random
import math

# 找出函数近似最值
s = 2
h = 0.0000001  # 步长
maxi = 0
mini = 100
while s <= 3:
    new = s*s + 4*s*math.sin(math.radians(s))
    if new > maxi:
        maxi = new
    if new < mini:
        mini = new
    s += h
count = 0
for i in range(10000):
    x = random.uniform(2,3)
    y = random.uniform(mini, maxi)
    if x*x + 4*x*math.sin(math.radians(x)) <= y:
        count += 1
result = count/10000 * (maxi - mini)
print(count)
print(result)
print(maxi, mini)
