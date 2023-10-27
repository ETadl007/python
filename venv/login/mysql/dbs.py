import pymysql
from venv.login.mysql import sql_list
from venv.login import test

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'py',
    'password': '123456',
    'db': 'pymysql',
    'charset': 'utf8'
}
db = pymysql.connect(**config)
cursor = db.cursor()


def insert(user_info):
    cursor.execute(sql_list.insert(), user_info)
    result = cursor.rowcount
    if result == 1:
        print("注册成功")
    else:
        print("有误")
    db.commit()


def is_user_exists(username):
    cursor.execute(sql_list.select(), username)
    result = cursor.rowcount
    if result == 1:
        print("用户名已存在")
        return True


def is_login(user_info):
    cursor.execute(sql_list.login(), user_info)
    result = cursor.fetchone()
    if result:
        print("登录成功 \n欢迎%s进入系统" % user_info["username"])
        test.login_success(user_info["username"])
    else:
        print("用户名或密码错误")
        test.login()


def update_user(new_name):
    cursor.execute(sql_list.update_username(), new_name)
    result = cursor.rowcount
    if result == 1:
        print("用户信息修改成功")
        test.login_success(new_name)
    else:
        print("用户信息修改失败")
        test.login_success(new_name)


def update_password(user_info):
    cursor.execute(sql_list.update(), user_info)
    result = cursor.rowcount
    if result == 1:
        print("密码修改成功")
        test.login_success(user_info)
    else:
        print("密码修改失败")
        test.login_success(user_info["username"])


def delete_user(username):
    cursor.execute(sql_list.log_off(), username)
    result = cursor.rowcount
    if result == 1:
        print("用户删除成功")
        test.login()
    else:
        print("用户删除失败")


def get_user_info(username):
    cursor.execute(sql_list.select(), username)
    result = cursor.fetchone()
    return result


# db.close()

def update_phone(phone):
    cursor.execute(sql_list.update_phone(), phone)
    result = cursor.rowcount
    if result == 1:
        print("手机号修改成功")
        test.login_success(phone)
    else:
        print("手机号修改失败")
        test.login_success(phone)
