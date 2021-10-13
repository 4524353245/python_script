#!/usr/bin/python
# -*- coding:utf-8 -*-

from tkinter import *
import pandas as pd
import os
import re
import sys

# 创建窗口
window = Tk()

# 窗口名称
window.title('数据匹配')

# 设计窗口的大小
window.geometry('300x400')

# 输入栏内容
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()
var7 = StringVar()

# 初始化输入栏
L1 = Label( text="请输入表A的名称：")
L1.pack()
e1 = Entry(window,show=None,textvariable=var1)
e1.pack()

L2 = Label( text="请输入表A中sheet名称：")
L2.pack()
e2 = Entry(window,show=None,textvariable=var2)
e2.pack()

L3 = Label( text="请输入表A中的ID列：")
L3.pack()
e3 = Entry(window,show=None,textvariable=var3)
e3.pack()

L4 = Label( text="请输入表B的名称：")
L4.pack()
e4 = Entry(window,show=None,textvariable=var4)
e4.pack()

L5 = Label( text="请输入表B中sheet名称：")
L5.pack()
e5 = Entry(window,show=None,textvariable=var5)
e5.pack()

L6 = Label( text="请输入表B中的ID列：")
L6.pack()
e6 = Entry(window,show=None,textvariable=var6)
e6.pack()

L7 = Label( text="请输入要匹配的表B中的列名：")
L7.pack()
e7 = Entry(window,show=None,textvariable=var7)
e7.pack()
A_id = e3.get() 

def data_match():

    # 获取当前路径

    os.chdir(sys.path[0])

    # 表1的路径
    table_a_path = e1.get()
    # 使用正则匹配当前文件1的类型
    a_type = re.search(r'([a-z]*).([a-z]*)',table_a_path).group(2)
    
    # 表1的sheet名称
    sheet_a_name = e2.get()
    A_id = e3.get()

    # 判断文件的类型
    if a_type == 'xlsx':
        table_a = pd.read_excel(table_a_path,sheet_name = sheet_a_name,converters={A_id:str}).dropna(axis=1,how='all',)
    else:
        table_a = pd.read_csv(table_a_path, sheet_name=sheet_a_name, converters={A_id: str}).dropna(axis=1, how='all')
    
###########################################################################################################################

    # 表2的路径
    table_b_path = e4.get()
    # 使用正则匹配当前文件2的类型
    b_type = re.search(r'([a-z]*).([a-z]*)',table_b_path).group(2)

    # 表2的sheet名称
    sheet_b_name = e5.get()
    B_id = e6.get()

    target_col = e7.get()


    if b_type == 'xlsx':
        table_b = pd.read_excel(table_b_path, sheet_name=sheet_b_name, converters={B_id: str}).dropna(axis=1, how='all',)
    else:
        table_b = pd.read_csv(table_b_path, sheet_name=sheet_b_name, converters={B_id: str}).dropna(axis=1, how='all')
    
    # table_b_2 = table_b.groupby(['B_id'])[target_col].sum().reset_index()

    table_c = pd.merge(table_a, table_b, how='left',on=[A_id])
    table_c.to_excel('c.xlsx',index=False)


# 按钮触发匹配
b = Button(window,text='进行匹配',width=15,height=2,command=data_match)
b.pack()
# 循环执行
window.mainloop()
