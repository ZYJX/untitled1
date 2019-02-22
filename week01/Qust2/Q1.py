p = input("输入手机号码进行验证")
a = [135,136,137,138,139,188,189,187,186]
try:
    int(p)
    if(len(p)==11):
        head = p[0:3]
        bool = False
        for i in a:
            if(int(head)== i):
                bool = True
                break
        if(True):
            print('手机号码有效')
        else:
            print('手机号码无效')
    else:
        print('手机号码不是有效的手机号码')
except ValueError:
    print('请正确输入数字')