# ------------------------字典（非常重要！！！！）----------------
# 4.1 字典的概述
# 首先，字典是以键值对的形式存储数据的
# 字典的表示方式：{key1:value,key2:value,key3:value}
dic = {"Mei":"攻", "Kiana":"受"} #通过key去找value
val = dic["Mei"] #用起来就是把索引换成key
print (val) #输出 攻

#字典的key必须是可哈希的数据类型
#字典的value可以是任何数据类型
dic = {"Mei":["Mei1","Mei2"]}



# 4.2 字典的增删改查

# a. 字典的新增和修改
dic = dict() #创建空字典
dic['Mei'] = "攻"
dic[1] = 123
print(dic) #输出{'Mei': '攻', 1: 123}
dic['Mei'] = '受'
print(dic) #此时，字典已经有了key的值，再次输入会更新 输出{'Mei': '受', 1: 123}

dic.setdefault("Bronia",1) #设置默认值，如果以前有key的值，那么就不起作用
dic.setdefault("Bronia",3)
print(dic) #输出{'Mei': '受', 1: 123, 'Bronia': 1}

# b. 删除
dic.pop('Mei')
print(dic) #输出{1: 123, 'Bronia': 1}

# c. 查询
print(dic['Bronia']) #输出1，但是如果key不存在，程序会报错，当你确定key没问题，可以用

print(dic.get('Bronia')) #输出1，但是key不存在，程序返回None，当你不确定key的时候，可以用

# 介绍None
a = None #单纯的就是空，表示没有的意思，什么都做不了
print(type(a)) #输出<class 'NoneType'>
s = '' #这是空字符串

#例子
dic = {'Mei': 1, 'Kiana': 2, 'Bronia': 3, }
name = input("请输入名字：")
val = dic.get(name)
if val is None:
    print("查无此人")
else:
    print(val)


# 4.3 字典的循环遍历和嵌套
dic = {'Mei': 1, 'Kiana': 2, 'Bronia': 3, }

#1. 可以使用for循环直接拿到key
for key in dic:
    print(key,dic[key]) # 输出Mei 1 Kiana 2 Bronia 3

#2. 希望把所有的key全都保存在列表中
print(dic.keys()) #拿到所有的key 输出dict_keys(['Mei', 'Kiana', 'Bronia'])
print(list(dic.keys())) #拿到所有keys并做成列表 ['Mei', 'Kiana', 'Bronia']

#3. 希望把所有的value都放在一个列表中
print(list(dic.values()))  #输出[1, 2, 3]

#4. 直接拿到字典中的key和value
print(list(dic.items())) #[('Mei', 1), ('Kiana', 2), ('Bronia', 3)]

for item in dic.items():
    key = item[0]
    value = item[1]
    print(key,value) #输出Mei 1 Kiana 2 Bronia 3

a, b = (1, 2) #元组或者列表都可以执行该操作，该行为被称为解构和解包
print(a)
print(b) #输出1 2
#如果元素过多会报错比如a, b = (1, 2, 3)：ValueError: too many values to unpack (expected 2)

for item in dic.items():
    print(item) #输出('Mei', 1) ('Kiana', 2) ('Bronia', 3) 输出的是元组
    #可以确定item只有两项元素，那么就可以：
    key, value = item
    print(key, value) #输出Mei 1 Kiana 2 Bronia 3

#继续化简：-----------(非常重要)！！！-----------------
for key,value in dic.items():
    print(key,value) #输出：Mei 1 Kiana 2 Bronia 3

# 字典的嵌套
Mei = {
    "name":'Mei',
    "wife": {
        'name':'Kiana',
        'sex':'female',
        'ability':{
            'name':'stop time',
            'age':18,
            'hobby':'girl'
        }
    },
       "friend":[
           {'name':'Bronia','age':14},
           {'name':'Seele','age':14},
           {'name':'Fuhua','age':500},
       ]
}
 #寻找Mei wife的ability的name
s = Mei['wife']['ability']['name']
print(s) #输出stop time

#给Mei第二个friend加一岁
Mei['friend'][1]['age'] = Mei['friend'][1]['age'] + 1
print(Mei)

# 4.4 补充：字典的循环删除

dic = {'Mei': 1, 'Kiana': 2, 'Bronia': 3, }

"""for key in dic:
    if key.startswith('M'):
        dic.pop(key)
print(dic) #输出报错RuntimeError: dictionary changed size during iteration
# 简言之不能直接删，也准备临时列表 """

# 删除的正确方式
temp = [] #存放即将要删除的key
for key in dic:
    if key.startswith('M'):
        temp.append(key)
        #dic.pop(key)
for t in temp:
    dic.pop(t)
print(dic)
