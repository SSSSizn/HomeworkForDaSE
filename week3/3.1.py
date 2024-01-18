number = float(input())
number1 = int(number)
number2 = number - number1
final = ""
final += bin(number1)[2:] + '.'
test = number2
while test - int(test) > 0:
    number2 *= 2
    number3 = int(number2)
    final += str(number3)
    number2 -= number3
    test *= 10
print(final)



