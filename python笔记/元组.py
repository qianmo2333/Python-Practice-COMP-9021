# -----------------Ԫ�� tuple--------------------
# Ԫ�� �ص㣺���ɱ���б�
import asyncore


t = ('Lisa', 'Anna')
print(t) #('Lisa', 'Anna')
print(t[1]) #���Anna
#t[0] = 'kiana' �ᱨ��'tuple' object does not support item assignment

#�̶���ĳЩ���ݲ���������޸ģ���ʹ��Ԫ��
#Ԫ��ֻ��һ��Ԫ��ʱ
t = ('Kiana') #����Ĭ�������ȼ�
print(t)
print(type(t)) #���<class 'str'>�����ַ���

s = ('Kiana', )
print(type(s)) #���<class 'tuple'>����Ԫ����

#Ԫ��Ĳ��ɱ䣨�ӣ����ڴ��ַ���ܱ�
a = (1,2,3, ['Kiana','Mei'])
a[3].append('Bronia')
print(a) #���(1, 2, 3, ['Kiana', 'Mei', 'Bronia'])���Ը��б������Ԫ�أ����ǲ��ܶ������б�