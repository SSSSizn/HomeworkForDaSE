n = int(input())
ans = 1
if n == 1:
    print("n的阶乘为1")
    exit(1)
while n > 1:
    ans *= n
    n -= 1
print("n的阶乘为", ans)
