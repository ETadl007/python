#导入copy模块
import copy
#1.创建一个空列表lst
lst = []
#2.在lst列表中依次追加10个数值(78, 93, 66, 83, 100, 95, 77, 93, 85, 98)；
x = [78, 93, 66, 83, 100, 95, 77, 93, 85, 98]
for i in x:
    lst.append(i)

#3.输出lst列表中第7个元素的数值；
print(lst[6])

#4.输出lst列表中第1~5个元素的数值；
print(lst[0:5])

#5.调用insert()函数，在lst列表第7个元素之前添加数值59；
lst.insert(6,59)
print(lst)

#6.利用变量num保存数值93，调用count()函数，查询num变量值在lst列表中出现的次数；
num = 93
print(lst.count(num))

#7.使用in查询lst列表中是否有num的变量值；
print(93 in lst)

#8.调用del()函数删除lst列表中的第1个元素；
del lst[0]

#9.调用sort()函数，对列表中所有元素进行排序，输出列表中最高分和最低分；
lst.sort()
print(lst[0],lst[-1])

#10.调用reverse()函数，颠倒lst列表中元素的顺序；
lst.reverse()
print(lst)

#11.调用pop()函数删除lst列表中尾部的元素，返回删除的元素；
print(lst.pop())

#12.lst列表中用append()函数追加数值83，并输出。调用remove()函数删除lst列表中第一个数值83；
lst.append(83)
print(lst)

#13.创建2个列表lst1和lst2，lst1中包含2个元素值：78，91，lst2中包含3个元素值：84，92，65，合并这两个列表，并输出全部元素；
lst1 = [78,91]
lst2 = [84,92,65]
lst1.extend(lst2)
print(lst1)

#14.创建lst1列表，其中包含数值2个元素值：78，91，将lst1中元素赋值5遍保存在lst2列表中，输出lst2列表中全部元素;
lst1 = [78,91]
lst2 = lst1 * 5
print(lst2)

#15.清空lst列表，将lst2列表复制给lst列表，将lst列表中第2个元素变为2，并分别输出lst列表、lst2列表全部元素。
lst.clear()
lst = copy.copy(lst2)
lst[1] = 2
print("lst列表：" ,lst)
print("lst2列表：", lst2)