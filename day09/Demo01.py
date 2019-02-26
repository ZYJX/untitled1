# 列表numbers中存储了一组数，numbers = [ 1, 5, -12, 37, 6,93, 100 ]，将这组数按照奇数偶数分别存储到两个列表even和odd中。
numbers = [1, 5, -12, 37, 6,93, 100]
even = []
odd = []
for i in numbers:
    if i%2 == 0:
        even.append(i)
    elif i%2 != 0:
        odd.append(i)
print('偶数=',even)
print('奇数=',odd)