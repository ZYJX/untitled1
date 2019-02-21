# 2. 编写程序，生成一个包含50个随机整数的列表，随机整数的范围是从-10到10，
# 然后将列表中所有的正数存为一个新的子列表，负数存为另一个新的子列表。
# （15分：生成随机列表5分，得出正负数新列表各5分）
import random
a = []
z = []
f = []
for i in range(50):
    b = random.randrange(-10, 11)
    # 生成一个包含50个随机整数的列表
    a.append(b)
    # 正数存为一个新的子列表
    if b>=0:
        z.append(b)
    # 负数存为另一个新的子列表。
    elif b<0:
        f.append(b)
#    全部输出
print(a)
print(z)
print(f)
