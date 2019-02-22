# 2. 判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，
# 如果能被整除，则表明此数不是素数，反之是素数。（30分）
a = []

for i in range(101,201):
    b = 0
    for j in range(2,i):
        if i%j==0:
            b += i
    if b == 0:
        a.append(i)
print(a)
print(len(a))



