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
# myName = input("请输入姓名：")
# myAge = int(input("请输入年龄："))
# myNo = input("请输入学号")
# print(f"我的年龄是：{myAge},我的姓名是：{myName},我的学号是：{myNo}")

"""
二、字符串的常规用法
    1.查找和替换
    字符串查找：在原文串中找到指定的字串
    格式：str.find(sub[,start,end])
    Str：原文串
    Sub：字串
    Start：查找起始位置，默认从0开始
    end：查找结束位置，默认最后一个字符
    返回值：如果没有找到则返回-1，如果找到了则返回第一次出现的下标，并且只返回第一次出现的下标
    
    2.替换：字符串中的字串替换成新的字串
    格式：str.rplace(old,new[,count])
    Old:标识被替换的字串
    New：新的字串
    Count：替换的次数，默认是全部替换
    返回值：如果原文串中存在要替换的字串，那么返回值替换后的完整字符在。如果存在要替换的字串，则返回原文串
    
    3.拼接：将若干个字符串合并生成一个新的字符串
    使用"+"号进行拼接
    使用join()方法进行拼接
    格式：str.join(i)
    i表示要拼接的字符在
    Str：拼接的字符
    
    4.删除
    在字符串的头部或者尾部删除制动的字符
    1.lstrip("字符")方法用于截掉字符串左边的空格（默认）或者指定字符
    2.rstrip()删除string字符串末尾的指定字符（默认是空格）
    3.Strip()删除字符串的头部和尾部的指定字符
    
    
"""
#查找字符串中的某个值，比如isW
str2 = "While there is life, there is hope"
r = str2.find("")
print(r)

#替换字符串中的某个值


#分割字符串
ip = "192.168.126.254"
new_ip = ip.replace(".",",",2)
rip = new_ip.split(".")
res = rip[0].replace(",",".")
print(res)

#字符串的拼接
