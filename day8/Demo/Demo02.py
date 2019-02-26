# 1. 编写函数，判断输入参数字符串是否为邮箱地址，检验条件为：字符串中间用@分隔，末尾是.com或者.net（40分）
import re
a = re.compile("\w+@+\w+\.+com")
b = input('输入参数字符串判断是否为邮箱地址')
em = re.search(a,b)
if em:
    print("输入正确")
else:
    print('输入错误')

# 2.编写程序，包含try…except…else …finally各个分支内语句,通过调用测试每个分支运行正确（20分）


try:
    a = input('输入一个数字')
    if a == int:
        print("输入正确")
except ValueError:
    print('不是一个数字')