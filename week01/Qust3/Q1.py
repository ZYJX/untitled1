p = input('请输入手机号')
a = [135,136,137,138,139]
# 通过异常判断是否为数字
try:
    int(p)
    # 判断手机号长度
    if(len(p)==11):
        h = p[0:3]
        bool = False
        # 判断手机号开头
        for i in a:
            if(int(h)==i):
                bool = True
                break
        if(bool):
            print("有效")
        else:
            print("无效")
    else:
        print("电话号码不规范")
except ValueError:
    print('请输入数字')