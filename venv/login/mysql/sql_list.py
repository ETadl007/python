# 查询用户信息
def select():
    return "SELECT * FROM account WHERE username = %s"

# 新增用户信息
def insert():
    return "INSERT INTO account (username, password, phone) VALUES (%(username)s, %(password)s, %(phone)s)"

# 删除用户信息
def delete():
    return "DELETE FROM account WHERE username = %(username)s"

# 修改用户密码
def update():
    return "UPDATE account SET password = %(new_password)s WHERE username = %(username)s AND password = %(" \
           "old_password)s"

# 登录
def login():
    return "SELECT * FROM account WHERE username = %(username)s AND password = %(password)s"

# 修改用户名
def update_username():
    return "UPDATE account SET username = %(new_name)s WHERE username = %(old_name)s"

# 注销用户
def log_off():
    return "DELETE  FROM account WHERE username = %s"

# 修改手机号
def update_phone():
    return "UPDATE account SET phone = %(new_phone)s WHERE phone = %(old_phone)s AND username = %(username)s"
