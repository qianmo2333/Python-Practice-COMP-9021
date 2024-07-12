# zip：把多个可迭代内容进行合并

lst1 = ["Bronia","Mei","Kiana"]
lst2 = ["14","16","16"]
lst3 = ["理律","雷律","空律"]

#目标：将列表的第一位放在一起
result = []
for i in range (len(lst1)):
    first = lst1[i]
    second = lst2[i]
    third = lst3[i]
    result.append((first,second,third)) 
print (result) #输出[('Bronia', '14', '理律'), ('Mei', '16', '雷律'), ('Kiana', '16', '空律')]

result = zip(lst1,lst2,lst3)
lst = list(result) #转化成列表模式
print(lst) # 输出[('Bronia', '14', '理律'), ('Mei', '16', '雷律'), ('Kiana', '16', '空律')]
