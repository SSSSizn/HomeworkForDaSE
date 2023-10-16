import re

id = input()
ret = re.match(r'^\d{6}((19\d{2})|((20[01]\d)|(202[0,3])))((0[13578]((0[1-9])|([1-2]\d)|30|31))|(02((0[1-9])|(1\d)|(2[0-8])))|(0[469]((0[1-9])|([1-2]\d)|30))|(11((0[1-9])|([1-2]\d)|30))|(12((0[1-9])|([1-2]\d)|30|31)))\d{3}([0-9]|x|X)$',id)
if ret:
    ret1 = re.match(r'^\d{10}(0229)\d{3}([0-9]|x|X)$',id)  # 是否为二月29号出生
    if ret1:
        ret2 = re.match(r'^\d{6}(19([02468][048]|[13579][26]))|(200[048]|201[26]|2020)\d{7}([0-9]|x|X)$',id)
        if ret2:
            print('该身份证号合法')  # 闰年出生
        else:
            print('该身份证号不合法')  # 非闰年出生
    else:
        print('该身份证号合法')  # 非二月29号出生

else:
    print('该身份证号不合法')

