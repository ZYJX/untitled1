# 1.用python语句判断所输入的手机号，是否正确
# 要对手机号的号段进行判断，号段任意给出6个作为模拟号段即可.
# 判断手机号码是否是由数字组成的(总分15分，5分能够判断是否为数字，
# 5分判断是否为有效号段，5分实现)
a = int(input("输入6位手机号码："))
# 判断是数字
if(type(a) == int):
    print('手机号码是由数字组成。')
    if (len(a)>=6):
        print('号码为有效号段')
    else:
        print('号码号段无效')
# 判断不是数字
elif (type(a) == str):
    print('手机号码有误，不是由数字组成。')