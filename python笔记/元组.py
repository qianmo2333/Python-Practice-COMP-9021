# -----------------元组 tuple--------------------
# 元组 特点：不可变的列表
import asyncore


t = ('Lisa', 'Anna')
print(t) #('Lisa', 'Anna')
print(t[1]) #输出Anna
#t[0] = 'kiana' 会报错：'tuple' object does not support item assignment

#固定了某些数据不允许外界修改，则使用元组
#元组只有一个元素时
t = ('Kiana') #（）默认是优先级
print(t)
print(type(t)) #输出<class 'str'>，是字符串

s = ('Kiana', )
print(type(s)) #输出<class 'tuple'>，是元组了

#元组的不可变（坑），内存地址不能变
a = (1,2,3, ['Kiana','Mei'])
a[3].append('Bronia')
print(a) #输出(1, 2, 3, ['Kiana', 'Mei', 'Bronia'])可以给列表里面加元素，但是不能动整个列表