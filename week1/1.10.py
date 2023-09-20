S = input()
length = len(S) - 1
i = 0
count = 1
while i < length:
    if S[i] == S[i+1]:
        count += 1
    i += 1
if count == 1:
    print("无连续相同字符")
else:
    print("有", count, "个连续相同字符")
