import re
import os
import copy


# 清空控制台输出
def clear():
    print()
    os.system('cls')
    return


# 验证
num = re.compile(r'[0-9]')
Special_cha = re.compile(r'[^0-9a-zA-Z]')
phone_num = re.compile(r'(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}')


# 只能是大小写字母或数字，且不能以数字开头，长度为5-12位 ^(?!\d+$)[\da-zA-Z]+$
def username_fun(username_f):
    if num.match(username_f) is None and Special_cha.search(username_f) is None and 5 <= len(username_f) <= 12:
        return True
    else:
        return False


# 第一次密码必须目只能由字母大小写和数字组成，长度为6-15位
def passwd_fun(passwd_f):
    if Special_cha.search(passwd_f) is None and 6 <= len(passwd_f) <= 15:
        return True
    else:
        return False


# 第二次密码必须和第一次相同
def password_fun(password_f, passwd_f):
    if password_f == passwd_f:
        return True
    else:
        return False


# 手机号验证
def phone_number_fun(phone_number_f):
    if phone_num.search(phone_number_f) is not None:
        return True
    else:
        return False


# 存储模块txt
# 插入
def interposition(info):
    with open("data.txt", "a", encoding="utf-8") as f:
        f.write(str(info))
        f.write("\n")
    return


# 读取匹配
def read(info):
    with open("data.txt", "r", encoding="utf-8") as f:
        line = f.readlines()
    for i in range(len(line)):
        dictionary = line[i].strip()
        dictionary = eval(dictionary)
        if dictionary["username"] == info["username"]:
            argument = 0
            return argument, dictionary
        elif dictionary["phone_number"] == info["phone_number"]:
            argument = 1
            return argument, dictionary
        elif i >= len(line) - 1:
            argument = 2
            return argument, dictionary


# 更改
def change(info, new_info, arg):
    with open("data.txt", "r", encoding="utf-8") as f:
        line = f.readlines()
        if arg == 0:
            line_1 = str(info) + "\n"
            line_2 = str(new_info) + "\n"
            line[line.index(line_1)] = line_2
        elif arg == 1:
            line_1 = str(info) + "\n"
            line.remove(line_1)
    with open("data.txt", "w", encoding="utf-8") as f:
        f.writelines(line)


# 注册程序
def register():
    clear()
    print("用户名格式为：只能字母数字组合，且不能以数字开头，长度为5-12位")
    username = input("请输入你的用户名：")
    if username == '退出':
        return 404
    while not username_fun(username):
        clear()
        print("用户名格式有误，请重新输入!!!")
        print("用户名格式为：只能字母数字组合，且不能以数字开头，长度为5-12位")
        username = input("请输入你的用户名：")
        if username == '退出':
            return 404
    clear()
    print("密码格式为：字母数字组合，且长度为6-15位")
    passwd = input("请输入你的密码：")
    if passwd == '退出':
        return 404
    while not passwd_fun(passwd):
        clear()
        print("密码格式有误，请重新输入!!!")
        print("密码格式为：字母数字组合，且长度为6-15位")
        passwd = input("请输入你的密码：")
        if passwd == '退出':
            return 404
    clear()
    password = input("请再次输入你的密码：")
    if password == '退出':
        return 404
    while not password_fun(password, passwd):
        clear()
        print("两次密码输入不一致，请重新输入!!!")
        password = input("请再次输入你的密码：")
        if password == '退出':
            return 404
    clear()
    phone_number = input("请输入你的手机号：")
    if phone_number == '退出':
        return 404
    while not phone_number_fun(phone_number):
        clear()
        print("手机号格式有误，请输入正确的手机号!!!")
        phone_number = input("请输入你的手机号：")
        if phone_number == '退出':
            return 404
    dict_register = {
        "username": username,
        "passwd": passwd,
        "phone_number": phone_number
    }
    clear()
    arg = read(dict_register)
    if arg[0] == 0:
        print("用户名已存在，注册失败")
    elif arg[0] == 1:
        print("电话号码已存在，注册失败")
    elif arg[0] == 2:
        interposition(dict_register)
        print("注册成功")
    return arg[0]


# 登录程序
def login():
    username = input("请输入你的用户名：")
    if username == "退出":
        res = 404
        return res, 0
    else:
        dict_login = {'username': username, 'phone_number': '?'}
        arg = read(dict_login)
        dictionary = arg[1]
        res = 4
        if arg[0] == 0:
            i = 0
            while True:
                passwd = input("请输入密码：")
                if dictionary['passwd'] == passwd:
                    print("登录成功")
                    res = 0
                    break
                elif passwd == "退出":
                    res = 404
                    return res, arg[1]
                else:
                    if i < 2:
                        i = i + 1
                        print("密码错误，还有%s次机会" % (3 - i))
                        continue
                    else:
                        print("登录失败")
                        res = 1
                        break
        else:
            clear()
            print("用户不存在")
            res = 2
        return res, arg[1]


# 登陆成功后选项
def login_suc(info):
    data = info.copy()
    while True:
        print("欢迎%s使用本系统" % info['username'])
        print("请输入编号选择：\n0.退出登录\n1.更改密码\n2.注销账号")
        select_l = input("请输入编号: ")
        if select_l == "0":
            clear()
            print("退出账号成功！！！")
            break
        elif select_l == "1":
            clear()
            print("欢迎%s使用本系统" % info['username'])
            print("密码格式为：字母数字组合，且长度为6-15位")
            new_passwd = input("请输入你的新密码：")
            if new_passwd == '退出':
                return 404
            while not passwd_fun(new_passwd):
                clear()
                print("密码格式有误，请重新输入!!!")
                print("密码格式为：字母数字组合，且长度为6-15位")
                new_passwd = input("请输入你的新密码：")
            clear()
            new_password = input("请再次输入你的密码：")
            if new_password == '退出':
                return 404
            while not password_fun(new_password, new_passwd):
                clear()
                print("两次密码输入不一致，请重新输入!!!")
                new_password = input("请再次输入你的新密码：")
            new_data = data.copy()
            new_data['passwd'] = new_password
            change(data, new_data, 0)
            data = new_data.copy()
            print("更改密码成功！！！")
        elif select_l == "2":
            clear()
            print("欢迎%s使用本系统" % info['username'])
            print("请输入编号选择：\n0.确认永久注销账号\n1.取消永久注销账号")
            select_ll = input("请输入编号: ")
            if select_ll == "0":
                change(info, 0, 1)
                print("永久注销账号成功！！！")
                clear()
                break
            elif select_ll == "1":
                print("取消永久注销账号成功！！！")
                clear()
        else:
            clear()
            print("请输入正确的编号！！！")


# 忘记密码程序
def forgot_password():
    clear()
    print('此功能待开发！！！！！')


# 主程序
if __name__ == '__main__':
    while True:
        print("在输入的地方输入‘退出’即可退出输入")
        print("请输入编号选择：\n0.退出程序\n1.注册\n2.登录\n3.忘记密码")
        select = input("请输入编号: ")
        if select == "0":
            break
        else:
            while True:
                if select == "1":
                    while True:
                        respond_r = register()
                        if respond_r == 404:
                            break
                        elif respond_r == 2:
                            break
                        else:
                            print("请输入编号选择：\n0.退出注册\n1.重新注册\n2.切换登录\n3.忘记密码")
                            select_1 = input("请输入编号: ")
                            if select_1 == "0":
                                clear()
                                break
                            elif select_1 == "1":
                                clear()
                                continue
                            elif select_1 == "2":
                                select = "2"
                                clear()
                                break
                            elif select_1 == "3":
                                select = "3"
                                clear()
                                break
                            else:
                                clear()
                                print("输入的编号不存在，请重新输入！！！")
                                continue
                    if select == "1":
                        break
                    else:
                        continue
                elif select == "2":
                    clear()
                    while True:
                        respond_l = login()
                        if respond_l[0] == 404:
                            print("退出成功！！！")
                            clear()
                            break
                        elif respond_l[0] == 0:
                            login_suc(respond_l[1])
                            break
                        elif respond_l[0] == 1:
                            print("请输入编号选择：\n0.退出登录\n1.重新登录\n2.切换注册\n3.忘记密码")
                            select_2 = input("请输入编号: ")
                            if select_2 == "0":
                                clear()
                                break
                            elif select_2 == "1":
                                clear()
                                continue
                            elif select_2 == "2":
                                select = "1"
                                clear()
                                break
                            elif select_2 == "3":
                                select = "3"
                                clear()
                                break
                            else:
                                print("输入的编号不存在，请重新输入！！！")
                                clear()

                    if select == "2":
                        break
                    else:
                        continue
                elif select == "3":
                    while True:
                        forgot_password()
                        select = ""
                        break
                    break
                elif select != "":
                    clear()
                    print("输入的编号不存在，请重新输入！！！")
                    break