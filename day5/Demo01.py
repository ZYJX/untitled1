# 1. 通过用户输入数字，计算阶乘。（30分）
a = 1
b = 0
d = 0
c = int(input("输入一个数字"))
# 根据输入的数进行判断循环次数
for i in range(1,c+1):
    b = a*i
    a = b
    d += a
print(d)

