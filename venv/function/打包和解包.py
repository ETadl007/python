# 打包
def test(*args):
    print(args)


test(1, 2, 3, 4)


# 解包
def test1(a, b, c, d):
    print(a, b, c, d)


t = [1, 2, 3, 4]
test1(*t)
