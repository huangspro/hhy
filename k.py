form xlrd import *
from xlwt import *
w=open_workbook()  #打开Excel文件
t=w.sheets()[0]    #获取第1个表
r=t.nrows          #获取有效行数
c=t.ncols          #获取有效列数
a=t.row_values(0)  #获取第1行的数据，结果以列表返回
b=t.col_values(0)  #获取第1列的数据，结果以列表返回