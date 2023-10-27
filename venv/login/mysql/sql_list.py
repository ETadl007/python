def select():
    return "SELECT username,phone FROM account WHERE username = %s"


def insert():
    return "INSERT INTO account (username, password, phone) VALUES (%(username)s, %(password)s, %(phone)s)"


def delete():
    return "DELETE FROM account WHERE username = %(username)s"


def update():
    return "UPDATE account SET password = %(new_password)s WHERE username = %(username)s AND password = %(" \
           "old_password)s"


def login():
    return "SELECT * FROM account WHERE username = %(username)s AND password = %(password)s"


def update_username():
    return "UPDATE account SET username = %(new_name)s WHERE username = %(old_name)s"


def log_off():
    return "DELETE  FROM account WHERE username = %s"


def update_phone():
    return "UPDATE account SET phone = %(new_phone)s WHERE phone = %(old_phone)s AND username = %(username)s"
