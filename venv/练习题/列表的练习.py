#已知列表1:4,5,2,7;列表2:3,6。将两个列表合并为一个列表，并且将合并后的列表按照降序排列输出
list1=[4,5,2,7]
list2=[3,6]
list1.extend(list2)
list1.sort(reverse=True)
print(list1)