#新建一个文件
f = open('test.txt','w')
# 关闭这个文件
f.close()

# 使用write向文件写入数据
f = open('test.txt','w')
f.write('hello world!')
f.close()

# 读数据
f = open('test2.txt','w')
f.close()

# 开始读
f = open('test.txt','r')
num = f.read(13)
print(num)
f.close()

# 写到第二个文件中
f = open('test2.txt','w')
f.write(num)
f.close()
