c = 2
g = c
while (g*g - c > 0.000001) or (c - g*g > 0.000001):
    g = (g + c/g)/2
print("起始值为c时，g=", g)

c = 2
g = c/2
while (g*g - c > 0.000001) or (c - g*g > 0.000001):
    g = (g + c/g)/2
print("起始值为c/2时，g=", g)

c = 2
g = c/4
while (g*g - c > 0.000001) or (c - g*g > 0.000001):
    g = (g + c/g)/2
print("起始值为c/4时，g=", g)

c = 2
g = c/8
while (g*g - c > 0.000001) or (c - g*g > 0.000001):
    g = (g + c/g)/2
print("起始值为c/8时，g=", g)

