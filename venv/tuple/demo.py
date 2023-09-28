# t = ('王炮',18,'男','03220843','智信2208')
# for i in t:
#     print(i)

list_one = [666,666,5,51,2,3,4,5,5,4]
list = []
for i in list_one:
    if i not in list:
        list.append(i)
        list.sort()
print(list)

t = ('a','b','c',[1,2,3])
t[3].append(4) #有风险，不推荐
print(t)
