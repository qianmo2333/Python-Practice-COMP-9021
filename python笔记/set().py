# ---------------------集合----------------------------
# set() 内部无序
s = {1, 2, 3}
print(type(s)) #<class 'set'>
# s = {1,2,3,"aha!",[]}
# print(s) TypeError: unhashable type: 'list'
# set集合要求存储的数据必须可以进行哈希计算
# 列表是[]，字典，set集合是不可哈希（可以进行增删改查）
# 整数，字符串，元组，布尔都是可哈希（不可变）
# 总结：可变的数据类型就是不可哈希的
s = set() #创建空集合
#set集合没有索引且乱序，pop默认弹出最后一个
s.add('Mei')
s.add("Bronia")
print(s)
# s.pop() 扔出去无序,不常用
s.remove('Bronia')
print(s) #输出{'Mei'}
#想要修改替换，也必须先remove再add

#查询，通过循环实现
for item in s:
    print(item) #输出Mei