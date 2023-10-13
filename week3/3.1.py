number = int(input())
if number != 0:
    test = 1
    while test <= number:
        test *= 2
    test = int(test / 2)
    final = 0
    while test != 1:
        if number >= test:
            number -= test
            final += 1
        final *= 10
        test = int(test / 2)
    if number == 1:
        final += 1
else:
    final = 0
print(final)



