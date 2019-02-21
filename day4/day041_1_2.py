# 2.二 输入一个数求1！+2！+3！+4！+n！=？
n = int(input('输入一个数'))
a = 1
b = 0
for i in range(1,n+1):
    a = a*i
    b += a
print(b)
