phone = input('请输入手机号码：')
list = [153,155,188,187,136,189]
try:
    int(phone)
    if(len(phone) == 11):
        str = phone[0:3]
        bool = False
        for i in list:
            if int(str) in list:
                bool = True
                break
        if(bool):
            print('手机号码符合')
        else:
            print('无效的手机号')
    else:
        print('手机号码不符合')
except ValueError:
    print('输入有误')