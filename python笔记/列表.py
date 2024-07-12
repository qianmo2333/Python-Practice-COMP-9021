#--------------------列表--------------------
#在python中用[]来表示一个列表，列表中的元素用逗号隔开
a = ['Lisa', 'Mary', [1,2,3]]
#4.1 特性
# 1. 与字符串一样有索引与切片
# 2. 列表的索引如果超过范围会报错
# 3. 可以用for循环进行遍历
# 4. 用len可以拿到列表长度
lst = ['Lisa', 'Mary','John','AAAA']
print(lst[0])  #输出Lisa
print(lst[1:3]) #输出['Mary', 'John']
print(lst[::-1]) #输出['AAAA', 'John', 'Mary', 'Lisa']
for item in lst:
    print(item)  #输出lst的所有值
print(len(lst)) #输出列表长度 4


#4.2 列表的增删改查（很重要）
lst = []
#向列表中添加内容
#append() 追加
lst.append("Lisa")
lst.append("John")
#insert() 插入
lst.insert(0, "Mary") #输出['Mary', 'Lisa', 'John']，其它均挪一位
print(lst)
#extend() 可以合并两个列表，批量的添加
lst.extend(['Aha', 'ABBB'])
print(lst) #输出['Mary', 'Lisa', 'John', 'Aha', 'ABBB']

# 删除
ret = lst.pop(3)
print(lst) #输出['Mary', 'Lisa', 'John', 'ABBB']
print(ret) #输出Aha，返回了pop出去的值
lst.remove("ABBB") #删除某个元素
print(lst) #输出['Mary', 'Lisa', 'John']

#修改
lst[2] = "aha!" #直接用索引就可以修改
print(lst) #输出['Mary', 'Lisa', 'aha!']

#查询 直接用索引进行查询
print([lst[1]]) #输出['Lisa']

#practice：(非常重要！！！！！！！)
#将所有的Mei换成Bronia
lst = ['Mei A', 'Mei B', 'Mei C', 'Mei D', 'Kiana']
#for item in lst: #此时看不到元素的索引位置
for i in range(len(lst)): #直接拿到列表索引的for循环
    item = lst[i] #item依然是列表中的每一项
    if item.startswith('Mei'):
        new_name = 'Bronia'+item[3:]
        print(new_name)
        #把新名字丢回列表（需要索引）
        lst[i] = new_name #修改完成
print(lst)


#4.3 列表的其他操作
# 排序
lst = [222,444,555,333,88,999,335]
lst.sort() #对列表进行排序
lst.sort(reverse = True) #reverse: 翻转
print(lst) #输出：[999, 555, 444, 335, 333, 222, 88]

#列表的嵌套
lst = ['abc','def',['aha!', ['Breathe'],'ahaaha'], 'rde','pqr']
#找出Breathe
print(lst[2][1][0]) #输出第二个列表里面的第一个列表里的第零个字符
lst[2][1][0] = lst[2][1][0].upper()
print(lst)

#列表的循环删除（难）
lst = ['Mei A', 'Mei B', 'Mei C', 'Mei D', 'Kiana']

temp = [] #准备一个临时列表，负责存储要删除的内容
for item in lst:
    if item.startswith('Mei'):
        temp.append(item) #把要删除的内容记录下来
        #list.remove(item)

for item in temp:
    lst.remove(item) #去源列表中进行删除
print(lst)

#安全稳妥的循环删除方式：将要删除的内容保存在一个新列表中，然后循环新列表，删除老列表