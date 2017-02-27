#coding:utf-8
import pandas as pd
import os
import csv

# 设置读取csv路径数组及文件名数组
csvdir = [r'e:/Test', r'D:/Test']
filename = [u'a.csv', u'b.csv']
for i in range(len(csvdir)):
  os.chdir(csvdir[i])
  csv = open(filename[i])
  data = pd.read_csv(csv)
  data.columns = [u'日期',u'姓名',u'收入',u'利润']
  print data[[u'日期', u'收入', u'利润']].groupby(u'日期').sum().reset_index()
