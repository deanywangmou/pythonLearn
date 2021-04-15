import xlsxwriter
import  xlrd
# # todo 创建excel文件
# xl = xlsxwriter.Workbook(r'insert.xlsx')
#
# # todo 添加sheet
# sheet = xl.add_worksheet('写入表格')
#
# # todo 往单元格cell添加数据,索引写入
# sheet.write_string(0, 0, 'username')
#
# # todo 位置写入
# sheet.write_string('B1', 'password')
#
# # todo 设置单元格宽度大小
# sheet.set_column('A:B', 30)
#
# # todo 关闭文件
# xl.close()


rd=xlrd.open_workbook(r'test.xlsx')
wr=xlsxwriter.Workbook(r'insert.xlsx')

#  获取原始文件sheet表
all_sheets=rd.sheet_names()
print (all_sheets)  #['订货商出货关系_20200817140249', 'test2']

#获取第一个sheet行数和列数
table=rd.sheets()[0]
rows=table.nrows
cols=table.ncols
print (rows,cols)

# todo 添加sheet
sheet=wr.add_worksheet(all_sheets[0])

#获取原始文件第一行内容
# row=table.row_values(0)
# print (row)

# todo 往单元格cell添加数据,索引写入
# # todo 往单元格cell添加数据,索引写入
# sheet.write_string(0, 0, 'username')
for i in range(rows):
    for j  in range(cols):
        row=table.row_values(i)# 获取第一行的内容,索引从0开始
        row1=str(row[j])[:-2]
        sheet.write_string(i,j,row1)

wr.close()







