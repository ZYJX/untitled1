# 4.实现100-200里面所有的质数字,打印这些质数并且求出个数
a = []
for i in range(100, 201):
    b = 0
    for x in range(2,i):
        if i%x==0:
            b += 1
    if b == 0:
        a.append(i)

print(a)
print(len(a))