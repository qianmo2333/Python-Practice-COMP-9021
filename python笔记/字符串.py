# -----------------------------------------------------------------------�ַ���------------------------------------------------------------------------------------------
#------------------------------------֪ʶ��1��printf���������������-----------------------------
name = input("�������")
age = input("����")
print(f"{name}, {age}")

#-----------------------------------֪ʶ��2����������Ƭ������������λ����ȡԪ�أ���Ƭ����һ���ַ�������ȡһ���֣�----------------------------
s = "�������ӳ�"
print(s[-1]) #��ʾ������һλ ���������
print(s[1:3])#����ȡ�ӵ�1λ�е�2 ��������š�����Ƭ�����[1,3)
print(s[3:])#��3�е�ĩβ ������ӳ���
print(s[:4])#��ͷ�е�3  ������������ӡ�
print(s[-3:-1]) #�����������е������ڶ���  ��������ӡ�
#������Ƭ����
s = "������"
print(s[::-1])#-1��ʾ�������� ����������ҡ�
#�﷨��s[start:end:step]��start�е�end��ÿstep��Ԫ�س���һ��Ԫ��
s = "abcdefghijklmnopqrst"
print(s[3:8:2]) #���ַ�����Ϊ��de����fg����h����stepΪ��ȡ��ߣ�stepΪ��ȡ�ұߣ������Ϊ��dfh��
print(s[2:11:3])#���Ϊcfi
print(s[-1:-10:-3])#stepΪ���������󣬷�Ϊ��tsr����qpo����nml�����������Ϊtqn

#-------------------------------------֪ʶ��3���ַ����ĳ������--------------------------------------------------------

#�ַ����Ĳ���һ�㲻���ԭ�ַ�������Ӱ�죬һ�㷵��һ���µ��ַ���

#3.1 �ַ�����Сдת��
s = "python"
s1 = s.capitalize()#�ò�������ʹ���ַ�������ĸ��д
print(s1)

s = "I have a dream!"
s1 = s.title() #���ʵ�����ĸ��д
print(s1)

s = "I HAVE A DREAM"
s1 = s.lower() #��������ĸ�������Сд��ĸ
print(s1)

s = "i have a dream"
s1 = s.upper() #��������ĸ������ɴ�д��ĸ(�ص�)
print(s1)

verify_code = "xAD1"
user_input = input(f"�������֤��:({verify_code})")
if verify_code.upper() == user_input.upper():
    print("Correct")
else:
    print("False")

#3.2 �ַ����и���滻
#strip() ȥ���ַ����������˵Ŀհ׷����ո�\t(����)��\n(���з�)��
s = "  hello, aa  bb  ccccc      "
s1 = s.strip()
print(s1)#���Ϊhello, aa  bb  ccccc���������˵Ŀո񶼱�ɾ��

#����
username = input("�������û�����").strip()
if username == "admin":
    print("Correct")

#replace(old, new) �ַ������滻
s = "Hello, I'm Lisa"
s1 = s.replace("Lisa","Mary")
print(s1)

#�ո��滻
a ="hello i am gay!"
a1 = a.replace(" ", "")#ȥ�����еĿո�
print(a1)

#split(��ʲô�и�)�ַ����и�,��ʲô�и�ͻ���ʧ��˭
a = "python_java_c_c#_javascript"
lst = a.split("_") #�и��Ľ�������б��У��ǳ���Ҫ��������
print(lst) #���Ϊ['python', 'java', 'c', 'c#', 'javascript']

#sumarry��replace()-->��a�滻��b,split()-->ɾ��ʹ���и��ﲢ���������ַ���ת����б�,strip()-->ɾ���ո���������

#3.3 ���Һ��ж�
#����
s = "Hello,I'm Lisa"
ret = s.find("Lisa")#����10����ΪL�ڵ�10λ���������-1����û���ҵ���
rob = s.index("Lisa")#����10����ΪL�ڵ�10λ����û�ҵ���ֱ�ӱ���
print(ret)
print("Lisa123123" in s)#������Ĳ��ң�û�ҵ���False���ҵ���True
print("Lis123" not in s)#�ж��Ƿ񲻴���

#�ж�
name = input("������������֣�")
#�ж����ǲ�������
if name.startswith("��"): #�ж��ַ����Ƿ���xxx��ͷ��endwith():�Ƿ���xxx��β
    print("������")
else:
    print("������")

money = input("�������㶵���Ǯ")
if money.isdigit(): #���ж��ַ����Ƿ����������
    print("��ү�����Ի�Ǯ��")
else:
    print("�Բ�������������")

#startswith(),isdigit(),in,not in,find

#3.4 ������ܽ�

#�������ú���len
s = "Hello"
print(len(s)) # length ����

#�������ú���join
lst = ['Lisa', 'Mary', 'John']
#ʹ��_���б��ڵ��ַ���������Ϊһ���ַ���
s = "_".join(lst)#�����Ϊ��Lisa_Mary_John
print(s)

