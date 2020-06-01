# LEGB
# L local 局部作用域
# E embeded 嵌套函数作用域
# G global 全局作用域
# B built-in 内置

count = 10
def test():
    count = 3
    print("count is %d"%(count))
test()
print("count is %d"%(count))