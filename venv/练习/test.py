while True:
    print("""
    1.选择用户注册
    2.选择用户登录
    3.退出
    """)
    new_name = input('请输入你选择的编号：>>>')
    if new_name == '1':
        print('进入用户注册程序')
        while True:
            username = input('请输入你的用户名>>>:').strip()
            password = input('请输入你的密码>>>:').strip()
            # 判断用户名是否存在
            with open(r'account.txt', 'r', encoding='utf8') as f2:
                for i in f2:
                    i1 = i.split('|')
                    if username == i1[0]:
                        print('用户已经注册')
                        break
                else:
                    # 1.2把用户输入的密码存到文件中
                    res = '%s|%s\n' % (username, password)
                    with open(r'account.txt', 'a', encoding='utf8') as f:
                        f.write(res)
                        print('{}注册成功'.format('username'))
                break
    # 2.1取出文件的内容
    elif new_name == '2':
        print('进入用户登录程序')
        user_name = input('请输入你的用户名>>>:').strip()
        user_password = input('请输入你的密码>>>:').strip()
        # 2.2读出文件内容
        with open(r'account.txt', 'r', encoding='utf8') as f1:
            for line in f1:
                line.split('|')
                if user_name == line.split('|')[0] and user_password == line.split('|')[1].strip('\n'):
                    print('登陆成功')
                    break
            else:
                print('登录失败')
    elif new_name == '3':
        break
    else:
        print('输入有误，请按提示输入')