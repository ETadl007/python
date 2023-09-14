#{}是占位符
#format的第一种方法
name = '炮师傅'
age = 18
no = '123456789'
str = '我的姓名是：{},我的年龄是：{},我的学号是：{}'
print(str.format(name,age,no))

#format的第二种方法（当不知变量有多少个时使用,占位符里面写变量名）格式如下：
str = '我的姓名是：{name},我的年龄是：{age},我的学号是：{no}'
print(str.format(name=name,age=age,no=no))

#format的第三种方法（按传入的顺序在占位符中写（类似下标）比如name是0，age是1）格式如下：
str = '我的姓名是：{0},我的年龄是：{1}，我的学号是：{2}'
print(str.format(name,age,no))

#f-string的使用方法
#格式 print(f"")
print(f"我的年龄是：{age},我的姓名是：{name},我的学号是：{no}")

#小练习(输入自己的信息并用f-string的方式输出出来)
myName = input("请输入姓名：")
myAge = int(input("请输入年龄："))
myNo = input("请输入学号")
print(f"我的年龄是：{myAge},我的姓名是：{myName},我的学号是：{myNo}")