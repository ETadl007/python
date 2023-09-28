str = "ffjshgfioshiwnjnfisjwm"
dic = {}
for i in str:
    if i  in  dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(dic)
