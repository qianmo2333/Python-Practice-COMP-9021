# -*- coding: utf-8 -*-
# �ļ�����
# 1. �ҵ�����ļ���˫����
# open(�ļ�·��,mode="",encoding="")
# �ļ�·����
#    1.����·��
#    2.���·��
# mode��
# r���Ȱ��Ķ�ȡ
#�ļ��򿪣�
open("Honkai3rd.txt")
open('../Honkai3rd.txt')
# ../ ָ��һ���ļ���
open('../file operating/Honkai3rd.txt')

#�ļ���ȡ��
f = open("Honkai3rd.txt", mode = "r", encoding="utf-8")
content = f.read()
print(content)