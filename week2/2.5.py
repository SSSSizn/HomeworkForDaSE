c = 2
g = c / 2
while (g*g - c > 0.000001) or (c - g*g > 0.000001):
    g = (g + c/g)/2
print("c = 2时，g =", g)

c = 20
g = c / 2
while (g*g - c > 0.000001) or (c - g*g > 0.000001):
    g = (g + c/g)/2
print("c = 20时，g =", g)


c = 200
g = c / 2
while (g*g - c > 0.000001) or (c - g*g > 0.000001):
    g = (g + c/g)/2
print("c = 200时，g =", g)

c = 2000
g = c / 2
while (g*g - c > 0.000001) or (c - g*g > 0.000001):
    g = (g + c/g)/2
print("c = 2000时，g =", g)

