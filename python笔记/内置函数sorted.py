# ����sorted

lst = [1,6,8,2,3,5,9,1]
s= sorted(lst)
print(s) #���[1, 1, 2, 3, 5, 6, 8, 9]
a = sorted(lst, reverse=True)
print(a) #���[9, 8, 6, 5, 3, 2, 1, 1]

lst = ["Bronia","Kiana","Mei","Seele","Fuhua"]
# sorted(lst, key=�������)
def func(item):#item��Ӧ�б���ÿһ������
    return len(item)
s = sorted(lst, key =func)
print(s) #���['Mei', 'Kiana', 'Seele', 'Fuhua', 'Bronia']

lst = [
    {"id":1,"name":"Mei","age":16},
    {"id":2,"name":"Bronia","age":14},
    {"id":3,"name":"Kiana","age":16},
    {"id":4,"name":"Fuhua","age":500},
    {"id":5,"name":"Seele","age":14}
]
#Ŀ�꣺���б��������
#1.����ÿ���˵������������
s = sorted(lst ,key =lambda d: d['age'])
print(s)

#��С��������
a = sorted(lst ,key =lambda d: d['age'], reverse=True)
print(a)