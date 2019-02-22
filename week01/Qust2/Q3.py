# 3. 编写程序，生成一个包含20个随机整数的列表，然后对其中偶数下标
# （下标即列表元素的索引）的元素进行降序排列，奇数下标的元素不变。
# （提示：使用切片。） (20分：生成列表5分，找到偶数下标8分，降序7分)
import random
a = []
for i in range(20):
    b = random.randrange(10)
    a.append(b)
print(a)
a[::2] = sorted(a[::2],reverse=True)
print(a)