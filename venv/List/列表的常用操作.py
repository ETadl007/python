"""
三、列表的常见操作
1.增加元素
2.查找元素
3.修改元素
4.删除元素
5.排序

"""
# 1.增加元素
list = ['小明','03220843','智信2208',20,'184664815','2栋']
#append() 方法用于在列表末尾添加新的列表（单个或列表）
old_list = ['php','python','java']
#使用循环方式
for i in old_list:
    list.append(i)
print(list)
#也可使用extend()方法将一个列表中的所有元素添加到另一个列表中
list.extend(old_list)
print(list)
#insert()方法用于将元素插入列表
list.insert(1,'insert')
print(list)


# 2.查找元素

# 3.修改元素
list[0] = "小红"
print(list)

# 4.删除元素
# remove() 方法用于移除列表中某个值
# list.remove(value)
# pop() 方法用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# list.pop(index)
# del list 从内存中删除列表
# del list[1] 删除指定下标的元素
# del list[index]
# clear() 方法用于清空列表
# list.clear()
print(list)

# 5.排序
list1 = [1,54,78,787,0,5,6,78]
# sorted() 方法用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数
# sort([key, reverse]) 默认升序排列
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的
# reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）

# reverse() 方法用于反向列表中元素
