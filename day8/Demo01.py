# 1.输入一个字符串，将该字符串反顺序输出（40分）
# import random
# list = input('请输入一个字符串进行排序：')
# # list1 = ''
# # # 该字符串反顺序输出
# # list = sorted(list,reverse=True)
# # print('反顺序输出',list)
#
# list2 = list[::-1]
# print(list2)
# 2.编写函数求三角形面积，输入参数为底边与高，输出面积（20分）
def m(a,b):
   mj = a*b*0.5
   print('三角形面积', mj)
a = int(input('输入三角形的底边：'))
b = int(input('输入上三角形的高：'))

m(a,b)

