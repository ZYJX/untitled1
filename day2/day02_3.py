# 1.编写Python程序判断字符串是否重复。（50分）
a = "Hello World"
list1 = list(a)
if (len(list1)!=len(set(list1))):
    print("重复")
else:
    print("不")
# 2.编写Python程序打印输出字符串中重复的所有字符。（50分）
