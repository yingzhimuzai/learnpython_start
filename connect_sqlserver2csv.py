#coding:utf-8
import pymssql
import os
import csv
import pandas as pd
from pandas.io import sql

csvdir = r'e:/Test'
os.chdir(csvdir)

# 建立连接
server = r'00.00.0.00'
user =  r'username'
password =  r'password'
conn = pymssql.connect(server, user, password, "test")
cursor = conn.cursor()
# 按每行写入csv
# cursor.execute(u'SELECT * FROM persons')
# sql_list = cursor.fetchmany()
# csvfile = file('all_user.csv', 'wb')
# writers = csv.writer(csvfile)
# writers.writerow(['id', 'name', 'state'])
# while 0:
#     lines = cursor.fetchmany()
#     if len(lines)==0:
#         break
#     for i in lines:
#         print i
#         writers.writerows([i])
# data.columns = row
# data.to_csv('test.csv')

# 存储为data写入csv
sql = u'SELECT * FROM persons'
data = pd.read_sql(sql,conn)
data.columns = ['id', 'name', 'state']
# 以最大id命名
file_name = str(data['id'].max())[:10]
data.to_csv(file_name + r'_alluser.csv',encoding='gbk',index=False)

conn.close()
