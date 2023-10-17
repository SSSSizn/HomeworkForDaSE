c = 2
h = 0.000001  # 步长
s = 1  # 起始值
while c - s*s > 0.000001:
    s += h
print(s)
