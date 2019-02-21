# 1.输入两个人的生日，比较两个人年龄大小
# print('输入第一个人的生日')
# a = int(input())
# print('输入第二个人的生日')
# b = int(input())
# print('两人年龄相差：', abs(a-b))
# 2.随机生成一个序列，再次生成一个整数，查看这个整数有没有在序列中
import random
A = []
for i in range(10):
    a = random.choice(range(10))
    A.append(a)
print(A)
b = random.choice(range(10))
if b in A:
    print(b)
    print('有')
else:
    print(b)
    print('没有')