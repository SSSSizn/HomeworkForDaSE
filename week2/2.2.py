import matplotlib.pyplot as plt

a = 2**10
b = 2**20
c = 2**30
d = 2**40
e = 2**50
print("2的10次方是", a)
print("2的20次方是", b)
print("2的30次方是", c)
print("2的40次方是", d)
print("2的50次方是", e)
print("由结果可以看出，随着平方次数的增加，结果增长速度加快")
input = [10, 20, 30, 40, 50]
result = [a, b, c, d, e]
plt.plot(input, result, marker='o', linestyle='-')
plt.title('2^x for different exponents')
plt.xlabel('exponent (x)')
plt.ylabel('2^x')
plt.grid(True)
plt.show()