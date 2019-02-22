import random
list = []
for i in range(50):
    num = random.randrange(-10, 11)
    list.append(num)
print(list)
z = []
f = []
for i in list:
    if(i > 0):
        z.append(i)
    elif i < 0:
        f.append(i)
print('正整数',z)
print('负整数',f)