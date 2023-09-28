import re
def check_user(username,password,phone):
    # 不能数字开头
    if username[0].isdigit() or len(username) < 5 and len(username) > 12:
        return print("用户名输入有误")
    if not re.match(r'^1[3-9]\d{9}$',phone):
        return print("手机号输入有误")
def reg_user():
    username = input("请输入用户名: ")
    password = input("请输入密码: ")
    phone = input("请输入手机号: ")

    if not check_user(username,password,phone):
        return
    user_info = {
        "username": username,
        "password": password,
        "phone": phone
    }
    return user_info

def store_user_info(user_info):
    users = []
    users.append(user_info)
    return users
def register():
    user_info = reg_user()
    user = store_user_info(user_info)
    return user

if __name__ == "__main__":
    print("欢迎注册")
    print("输入1注册 输入0退出")
    close = input("请输入: ")
    while True:
        if close == "0":
            print("退出成功")
            break
        elif close == "1":
            user = register()
            break
        else:
            print("输入有误")
            break