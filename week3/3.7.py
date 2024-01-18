a = int(input())
b = int(input())
if a > b:
    c = a % b
    if c == 0:
        print("最大公约数为", b)
    while c != 0:
        a = b
        b = c
        c = a % b
    print("最大公约数为", b)
elif b > a:
    c = b % a
    if c == 0:
        print("最大公约数为", b)
    while c != 0:
        b = a
        a = c
        c = b % a
    print("最大公约数为", b)
elif a == b:
    print("最大公约数为", b)
