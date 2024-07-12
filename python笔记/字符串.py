# -----------------------------------------------------------------------字符串------------------------------------------------------------------------------------------
#------------------------------------知识点1：printf输出任意数据类型-----------------------------
name = input("你的名字")
age = input("年龄")
print(f"{name}, {age}")

#-----------------------------------知识点2：索引和切片（索引：按照位置提取元素，切片：从一个字符串中提取一部分）----------------------------
s = "我是张子辰"
print(s[-1]) #表示倒数第一位 输出“辰”
print(s[1:3])#则切取从第1位切到2 输出“是张”；切片输出是[1,3)
print(s[3:])#从3切到末尾 输出“子辰”
print(s[:4])#从头切到3  输出“我是张子”
print(s[-3:-1]) #倒数第三个切到倒数第二个  输出“张子”
#控制切片方向
s = "我是张"
print(s[::-1])#-1表示从右往左 输出“张是我”
#语法：s[start:end:step]从start切到end，每step个元素出来一个元素
s = "abcdefghijklmnopqrst"
print(s[3:8:2]) #将字符分组为“de”“fg”“h”，step为正取左边，step为负取右边，故输出为“dfh”
print(s[2:11:3])#输出为cfi
print(s[-1:-10:-3])#step为负从右往左，分为“tsr”“qpo”“nml”，所以输出为tqn

#-------------------------------------知识点3：字符串的常规操作--------------------------------------------------------

#字符串的操作一般不会对原字符串产生影响，一般返回一个新的字符串

#3.1 字符串大小写转换
s = "python"
s1 = s.capitalize()#该操作可以使得字符串首字母大写
print(s1)

s = "I have a dream!"
s1 = s.title() #单词的首字母大写
print(s1)

s = "I HAVE A DREAM"
s1 = s.lower() #把所有字母都输入成小写字母
print(s1)

s = "i have a dream"
s1 = s.upper() #把所有字母都输入成大写字母(重点)
print(s1)

verify_code = "xAD1"
user_input = input(f"请输出验证码:({verify_code})")
if verify_code.upper() == user_input.upper():
    print("Correct")
else:
    print("False")

#3.2 字符串切割和替换
#strip() 去掉字符串左右两端的空白符（空格，\t(缩进)，\n(换行符)）
s = "  hello, aa  bb  ccccc      "
s1 = s.strip()
print(s1)#输出为hello, aa  bb  ccccc，左右两端的空格都被删除

#案例
username = input("请输入用户名：").strip()
if username == "admin":
    print("Correct")

#replace(old, new) 字符串的替换
s = "Hello, I'm Lisa"
s1 = s.replace("Lisa","Mary")
print(s1)

#空格替换
a ="hello i am gay!"
a1 = a.replace(" ", "")#去掉所有的空格
print(a1)

#split(用什么切割)字符串切割,用什么切割，就会损失掉谁
a = "python_java_c_c#_javascript"
lst = a.split("_") #切割后的结果放在列表当中（非常重要！！！）
print(lst) #输出为['python', 'java', 'c', 'c#', 'javascript']

#sumarry：replace()-->将a替换成b,split()-->删掉使用切割物并将处理后的字符串转变成列表,strip()-->删掉空格缩进换行

#3.3 查找和判断
#查找
s = "Hello,I'm Lisa"
ret = s.find("Lisa")#返回10：因为L在第10位（如果返回-1则是没有找到）
rob = s.index("Lisa")#返回10：因为L在第10位（但没找到会直接报错）
print(ret)
print("Lisa123123" in s)#更方便的查找，没找到报False，找到报True
print("Lis123" not in s)#判断是否不存在

#判断
name = input("请输入你的名字：")
#判断你是不是姓张
if name.startswith("张"): #判断字符串是否以xxx开头，endwith():是否以xxx结尾
    print("你姓张")
else:
    print("不姓张")

money = input("请输入你兜里的钱")
if money.isdigit(): #来判断字符串是否由整数组成
    print("少爷，可以花钱了")
else:
    print("对不起，您输入有误")

#startswith(),isdigit(),in,not in,find

#3.4 补充和总结

#关于内置函数len
s = "Hello"
print(len(s)) # length 长度

#关于内置函数join
lst = ['Lisa', 'Mary', 'John']
#使用_把列表内的字符连起来变为一个字符串
s = "_".join(lst)#输出即为：Lisa_Mary_John
print(s)

