"""
列表
一、列表的概念
列表：在内存中，连续存储多个数据的一种数据结构。可以通过下标访问列表中的任意元素。
正向索引：从左到右，从0开始，依次递增
反向索引：从右到左，从-1开始，依次递减
二、列表的使用
1.创建方法
list = [1,2,3,4,5,6,7,8,9]
方法二
使用list()函数
list1 = list("hello") 参数必须是一个可迭代对象
"""
from  collections.abc import Iterable #导入Iterable类

#不限制数据类型
list = [1, 2.5, 3, 4, 5, 6, 7, 8, 9,True,"hello"]
print(list)
list1 = ["王炮", 18, 188 ,'03220843', True]
print(list1)

#判断是否是可迭代对象
n = 'python'
r = isinstance(n, Iterable)
print(r)

#使用切片的方式访问数组中的元素
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list2[0:7:3])

#遍历数组
list3 = ['小明','03220843','智信2208',20,'184664815','2栋']
for i in list3:
    print(i)

