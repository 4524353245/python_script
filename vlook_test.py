import pandas as pd
import os
import re
import sys

os.chdir(sys.path[0])

# 表1的路径
table_a_path = 'a.xlsx'
# 使用正则匹配当前文件1的类型
a_type = re.search(r'([a-z]*).([a-z]*)',table_a_path).group(2)
    
# 表1的sheet名称
sheet_a_name = 'Sheet2'
A_id = 'csc号'

# 判断文件的类型
if a_type == 'xlsx':
    table_a = pd.read_excel(table_a_path,sheet_name = sheet_a_name,converters={A_id:str}).dropna(axis=1,how='all',)
else:
    table_a = pd.read_csv(table_a_path, sheet_name=sheet_a_name, converters={A_id: str}).dropna(axis=1, how='all')



# 表2的路径
table_b_path = 'b.xlsx'
# 使用正则匹配当前文件2的类型
b_type = re.search(r'([a-z]*).([a-z]*)',table_b_path).group(2)

# 表2的sheet名称
sheet_b_name = '国内学生'
B_id = '序号'

target_col = '性别'

if b_type == 'xlsx':
    table_b = pd.read_excel(table_b_path, sheet_name=sheet_b_name, converters={B_id: str}).dropna(axis=1, how='all',)
else:
    table_b = pd.read_csv(table_b_path, sheet_name=sheet_b_name, converters={B_id: str}).dropna(axis=1, how='all')

print(table_b.head())

# 不同的merge类型
# table_1 = pd.merge(table_a, table_b, on='CSC号', how='inner')

# left 按照left的dataframe为基准，右边值为空的话就默认nan
table_2 =  pd.merge(table_a, table_b, on='CSC号', how='outer')

table_2.to_excel('c.xlsx',index=False)