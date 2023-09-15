str = "Life is short, learn python, I use python"
if str.find("python") != -1:
    #替换Python首字母大写
    str = str.replace("python", "Python")
    print(str)
else:
    #原样输出
    print(str)