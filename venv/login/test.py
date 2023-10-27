import re
import os
from venv.login.mysql import dbs


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
    if dbs.is_user_exists(user_val):
        return True
    return False


def is_exit(is_val):
    if is_val == 'q':
        return False
    return True


def store_user_info(user_info):
    if dbs.insert(user_info):
        return True
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
        'username': username,
        'password': password,
        'phone': phone
    }

    if is_user_exists(username):
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
    account = {
        'username': username,
        'password': password
    }
    dbs.is_login(account)


def login_success(cur_user):
    print("0.退出登录\n1.返回用户注册\n2.修改用户名\n3.修改密码\n4.修改手机号\n5.查看个人信息\n6.注销此用户")
    close = input("请输入编号: ")
    while True:
        if close == "0":
            break
        elif close == "1":
            register()
            break
        elif close == "2":
            update_username(cur_user)
            break
        elif close == "3":
            login_success_update(cur_user)
            break
        elif close == "4":
            update_phone(cur_user)
            break
        elif close == "5":
            show_account(cur_user)
            break
        elif close == "6":
            delete(cur_user)
            break
        else:
            print("输入错误")
            login_success(cur_user)
            break


def update_username(cur_user):
    print("欢迎进入修改用户名程序")
    new_name = input("请输入新的用户名: ")
    if not is_val_username(new_name):
        return None
    info = {
        "new_name": new_name,
        "old_name": cur_user
    }
    dbs.update_user(info)


def update_phone(cur_user):
    print("欢迎进入修改手机号程序")
    this_phone = dbs.get_user_info(cur_user)
    print(f"请使用此手机号进行验证：{this_phone[1]}")

    old_phone = input("请输入旧的手机号：")
    new_phone = input("请输入新的手机号: ")
    if not is_val_phone_number(new_phone):
        return None
    info = {
        "username": cur_user,
        "new_phone": new_phone,
        "old_phone": old_phone
    }
    dbs.update_phone(info)


def login_success_update(username):
    print("欢迎进入修改密码程序")
    old_pass = input("请输入旧密码: ")
    new_pass = input("请输入新密码: ")

    info = {
        "username": username,
        "new_password": new_pass,
        "old_password": old_pass
    }
    dbs.update_password(info)


def show_account(this_user):
    print("欢迎进入查看个人信息程序")
    account = dbs.get_user_info(this_user)
    print(f"用户名: {account[0]}\n手机号：{account[1]}")
    print("0.退出")
    close = input("请输入编号: ")
    while True:
        if close == "0":
            break
        else:
            print("输入错误")
            show_account(this_user)
            break


def delete(cur_user):
    is_continue = input("您是否注销此用户  ---请输入'y/n'执行操作")
    if is_continue == 'y':
        print("确定注销用户？请输入'y'继续执行操作：")
        d = input()
        if d == 'y':
            dbs.delete_user(cur_user)
    else:
        print("取消用户注销")


if __name__ == "__main__":
    while True:
        print("欢迎进入用户管理系统")
        print("0.退出\n1.选择用户注册\n2.选择用户登录")
        choice = input("请输入编号: ")
        while True:
            if choice == "0":
                print("退出成功")
                exit(0)
            elif choice == "1":
                register()
                break
            elif choice == "2":
                login()
                break
            else:
                print("输入有误")
                break
