# 查询用户信息
select = "SELECT * FROM account WHERE BINARY username = %s"

# 查询用户信息
show_phone = "SELECT phone FROM account WHERE phone = %s"

# 新增用户信息
insert = "INSERT INTO account (username, password, phone) VALUES (%(username)s, %(password)s, %(phone)s)"

# 删除用户信息
delete = "DELETE FROM account WHERE username = %(username)s"

# 修改用户密码
update = "UPDATE account SET password = %(new_password)s WHERE username = %(username)s AND password = %(" \
         "old_password)s"

# 登录
login = "SELECT * FROM account WHERE BINARY username = %(username)s AND password = %(password)s"

# 修改用户名
update_username = "UPDATE account SET username = %(new_name)s WHERE phone = %(phone)s"

# 注销用户
log_off = "DELETE  FROM account WHERE username = %s"

# 修改手机号
update_phone = "UPDATE account SET phone = %(new_phone)s WHERE phone = %(old_phone)s AND username = %(username)s"
