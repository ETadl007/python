import re


def is_val_username(username):
    # 不能数字开头
    if username[0].isdigit() or len(username) < 5 and len(username) > 12:
        print("用户名只能包含大小写字母和数字，且不能以数字开头")
        register()
        return False
    if not (5 <= len(username) <= 12):
        print("用户名长度必须在5-12位之间")
        register()
        return False
    return True


def is_val_password(password):
    if not (6 <= len(password) <= 15):
        print("密码长度必须在6~15位之间")
        register()
        return False

    return True


def is_val_phone_number(phone):
    if not re.match(r'^1[3-9]\d{9}$', phone):
        print("手机号格式不正确")
        register()
        return False

    return True


# 判断用户是否存在
def is_user_exists(user_val):
    with open("account.txt", "r") as f:
        for line in f:
            name = eval(line)
            if user_val["username"] == name["username"]:
                return True
    return False


# 注册用户
def reg_user():
    username = input("请输入用户名: ").strip()
    if not is_val_username(username):
        return None
    password = input("请输入密码: ").strip()
    if not is_val_password(password):
        return None
    phone = input("请输入手机号: ").strip()
    if not is_val_phone_number(phone):
        return None
    user_info = {
        "username": username,
        "password": password,
        "phone": phone
    }

    return user_info


def store_user_info(user_info):
    if is_user_exists(user_info):
        print("用户名已存在")
        register()
    else:
        with open("account.txt", "a", encoding="utf-8") as f:
            f.write(str(user_info) + "\n")
            print('注册成功')
            f.close()
        return user_info


def register():
    user_info = reg_user()
    store = store_user_info(user_info)
    return store


def login():
    username = input("请输入用户名: ")
    password = input("请输入密码: ")
    with open("account.txt", "r", encoding="utf-8") as f:
        for line in f:
            # 将line转换为字典
            user_info = eval(line)
            if user_info["username"] == username and user_info["password"] == password:
                print("登录成功")
                break
            else:
                print("用户名或密码错误")
                break
        f.close()


def update():
    username = input("请输入用户名: ")
    old_pass = input("请输入旧密码: ")
    new_pass = input("请输入新密码: ")

    with open("account.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        user_info = eval(line)
        if user_info["username"] == username and user_info["password"] == old_pass:
            user_info["password"] = new_pass
            lines[i] = str(user_info) + "\n"
            print("修改成功")
            break
    else:
        print("用户名或密码错误")

    with open("account.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)
        f.close()


if __name__ == "__main__":
    print("欢迎进入用户管理系统")
    while True:
        print("0.退出\n1.选择用户注册\n2.选择用户登录\n3.修改密码")
        close = input("请输入编号: ")
        while True:
            if close == "0":
                print("退出成功")
                break
            elif close == "1":
                print("欢迎进入注册程序")
                user = register()
                break
            elif close == "2":
                print("欢迎进入登录程序")
                login()
                break
            elif close == "3":
                print("欢迎进入修改密码程序")
                update()
                break
            else:
                print("输入有误")
                break
