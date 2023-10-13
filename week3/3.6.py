grade = int(input())
if grade < 60:
    print("不合格")
elif 60 <= grade < 75:
    print("合格")
elif 75 <= grade < 90:
    print("良好")
elif grade >= 90:
    print("优秀")
