import re


def is_val_username(username):
    if not (5 <= len(username) <= 12):
        print("用户名长度必须在5-12位之间")
        register()
        return False
    if not username[0].isalpha():
        print("用户名只能包含大小写字母和数字，且不能以数字开头")
        register()
        return False
    return True


def is_val_password(password):
    if not (6 <= len(password) <= 15) or re.match(r'[^0-9a-zA-Z]', password):
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


def is_exit(is_val):
    if is_val == 'q':
        return False
    return True


def store_user_info(user_info):
    with open("account.txt", "a", encoding="utf-8") as f:
        f.write(str(user_info) + "\n")
        print('注册成功')
        f.close()
    return False


def register():
    print("欢迎来到注册程序 --->如不注册请输入q退出")
    print("**用户名只能包含大小写字母和数字，且不能以数字开头")
    username = input("请输入用户名: ").strip()
    if not is_exit(username):
        return None
    if not is_val_username(username):
        return None

    print("密码长度必须在6~15位之间")
    password = input("请输入密码: ").strip()
    if not is_exit(password):
        return None
    if not is_val_password(password):
        return None

    print("按照标准的国内手机号码规则进行校验")
    phone = input("请输入手机号: ").strip()
    if not is_exit(phone):
        return None
    if not is_val_phone_number(phone):
        return None
    user_info = {
        "username": username,
        "password": password,
        "phone": phone
    }

    if is_user_exists(user_info):
        print("用户名已存在")
        register()
        return

    store = store_user_info(user_info)
    return store


def login():
    print("欢迎进入登录程序--->如不注册请输入q退出")
    username = input("请输入用户名: ").strip()
    if not is_exit(username):
        return None
    password = input("请输入密码: ").strip()
    if not is_exit(password):
        return None
    with open("account.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        user = eval(line)
        if user["username"] == username and user["password"] == password:
            print("登录成功 \n欢迎%s进入系统" % username)
            login_success(username)
            break
    else:
        print("用户名或密码错误")


def login_success(cur_user):
    print("0.退出登录\n1.返回用户注册\n2.修改密码")
    close = input("请输入编号: ")
    while True:
        if close == "0":
            break
        elif close == "1":
            register()
            break
        elif close == "2":
            login_success_update(cur_user)
            break
        else:
            print("输入错误")
            login_success(cur_user)
            break


def login_success_update(username):
    print("欢迎进入修改密码程序")
    old_pass = input("请输入旧密码: ")
    new_pass = input("请输入新密码: ")

    with open("account.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        user = eval(line)
        if user["username"] == username and user["password"] == old_pass:
            user["password"] = new_pass
            lines[i] = str(user) + "\n"
            print("修改成功")
            break
    else:
        print("用户名或密码错误")

    with open("account.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)
        f.close()


if __name__ == "__main__":
    while True:
        print("欢迎进入用户管理系统")
        print("0.退出\n1.选择用户注册\n2.选择用户登录")
        choice = input("请输入编号: ")
        while True:
            if choice == "0":
                print("退出成功")
                break
            elif choice == "1":
                register()
                break
            elif choice == "2":
                login()
                break
            else:
                print("输入有误")
                break
