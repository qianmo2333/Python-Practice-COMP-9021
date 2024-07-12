# 匿名函数：
    # lambda表达式
    #语法：变量 = lambda 参数1，参数2，参数3... : 返回值

#帮我计算A+B的结果

def func(a,b):
    return a + b
ret = func(12,13)
print(ret)

fn = lambda a, b :a+b
ret = fn(12,13)
print(ret)

#作用：高效创建函数