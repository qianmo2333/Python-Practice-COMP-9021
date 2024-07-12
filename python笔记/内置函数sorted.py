# 排序：sorted

lst = [1,6,8,2,3,5,9,1]
s= sorted(lst)
print(s) #输出[1, 1, 2, 3, 5, 6, 8, 9]
a = sorted(lst, reverse=True)
print(a) #输出[9, 8, 6, 5, 3, 2, 1, 1]

lst = ["Bronia","Kiana","Mei","Seele","Fuhua"]
# sorted(lst, key=排序规则)
def func(item):#item对应列表中每一项数据
    return len(item)
s = sorted(lst, key =func)
print(s) #输出['Mei', 'Kiana', 'Seele', 'Fuhua', 'Bronia']

lst = [
    {"id":1,"name":"Mei","age":16},
    {"id":2,"name":"Bronia","age":14},
    {"id":3,"name":"Kiana","age":16},
    {"id":4,"name":"Fuhua","age":500},
    {"id":5,"name":"Seele","age":14}
]
#目标：对列表进行排序
#1.根据每个人的年龄进行排序
s = sorted(lst ,key =lambda d: d['age'])
print(s)

#从小到大排序
a = sorted(lst ,key =lambda d: d['age'], reverse=True)
print(a)