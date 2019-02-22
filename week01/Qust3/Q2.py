import random
a = []
for i in range(50):
    b = random.choice(range(-10,11))
    a.append(b)
print(a)
z = []
f = []
for i in a:
    if i>0:
        z.append(i)
    elif i<0:
        f.append(i)
print(z)
print(f)