# -*- coding: utf-8 -*-
# 文件操作
# 1. 找到这个文件，双击打开
# open(文件路径,mode="",encoding="")
# 文件路径：
#    1.绝对路径
#    2.相对路径
# mode：
# r：热爱的读取
#文件打开：
open("Honkai3rd.txt")
open('../Honkai3rd.txt')
# ../ 指上一层文件夹
open('../file operating/Honkai3rd.txt')

#文件读取：
f = open("Honkai3rd.txt", mode = "r", encoding="utf-8")
content = f.read()
print(content)