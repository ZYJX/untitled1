# 随机生成一个包含1000个字母的字符串，然后统计该字符串中每个字母的数量，
# 并输出结果（要求结果以字典方式存储）（20分：随机生成字符串5分，
# 统计字母数量8分，以字典方式存储5分，输出结果2分）
import random
str = 'abcd'
str1 = ''
# 随机生成一个包含1000个字母的字符串，
for i in range(1000):
   str1+=random.choice(str)
print("字符串长度",len(str1))

dict = {}
for i in str1:
    key = dict.get(i)
    # 每个字母的数量，
    if(key==None):
        dict[i] = 1
    else:
        dict[i] += 1
# 输出结果
print(dict)