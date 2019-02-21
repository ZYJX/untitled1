# 1.有一列分数序列，2／1，3／2，5／3，8／5。。。求出前20项之和
# a1 = 2
# b1 = 1
# s1 = 0
# for n in range(1,21):
#     s1 += a1/b1
#     t1 = a1
#     a1 = a1 + b1
#     b1 = t1
# print("前20项之和:",s1)

# 2.二 输入一个数求1！+2！+3！+4！+n！=？
# import math
# sum2 = 0
# num2 = int(input('请输入一个数字：'))
# for i2 in range(1,num2+1):
#     F=math.factorial(i2)
#     sum2 += F
# print(sum2)

# s2 = 0
# a2 = 1
# n2 = int(input('请输入一个数：'))
# for i2 in range(1,n2+1):
#     a2 = a2*i2
#     s2 += a2
# print(s2)



# 3.有四个数字1，2，3，4，能组成多少个互不相同的三位数
# a3 = []
# for i3 in range(1,5):
#     for j3 in range(1,5):
#         for k3 in range(1,5):
#             if(i3 !=j3)and(j3 !=i3)and(k3 !=j3):
#                 print(i3, j3, k3)


# 4.实现100-200里面所有的质数字,打印这些质数并且求出个数
# a = 100
# count = 0
# while a <= 200:
#     sum = 0
#     for i in range(2,a):
#         b = a%i
#         if(b == 0):
#             sum += 1
#     if(sum == 0):
#         print(a)
#         count += 1
#     a += 1
# print('质数的个数是：',count)
#
# a = []
# for i in range(100, 201):
#     b = 0
#     for x in range(2, i):
#         if i%x == 0:
#             b += 1
#     if b == 0:
#         a.append(i)
# print(a)
# print(len(a))

# 5.电脑随机生成1~100随机数，用户输入一个数字，电脑提示用户大或者小，猜错，继续提示；猜对，则程序终止。

import random
a5 = random.randrange(1,101)
while True:
    b5 = int(input("输入一个数字："))
    if a5>b5:
        print('小')
    elif a5<b5:
        print('大')
    else:
        print('猜对了')
        break