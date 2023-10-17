c = 10
g = c/2
while g*g*g - c > 0.000001 or c - g*g*g > 0.000001:
    g = (2*g + c/(g*g)) / 3
print(g)
