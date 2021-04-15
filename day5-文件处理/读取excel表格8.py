import  xlrd

# xl = xlrd.open_workbook(r'‪c:\Users\LENOVO\Desktop\test.xlsx')
xl = xlrd.open_workbook(r'test.xlsx')

# 通过索引获取要操作的工作表,如下为第一个sheet
table = xl.sheets()[0]
allSheetNames = xl.sheet_names();
print(table,allSheetNames)

# 1.2 按索引号获取sheet的名字（string类型）
sheet1Name = xl.sheet_names()[1];
print(sheet1Name);

# 获取一共多少行
rows = table.nrows
print('获取一共多少行',rows)

# 获取一共多少列
cols=table.ncols
print ('获取一共多少列',cols)

# 获取第一行的内容,索引从0开始
row = table.row_values(0)
print ('获取第一行的内容,索引从0开始',row)

# 获取第一列的整列的内容
col = table.col_values(0)
print ('获取第一列的整列的内容',col)
# 获取第一列，第0~4行（不含第4行）
print('获取第一列，第0~4行（不含第4行）',table.col_values(0,0,4))

# 获取单元格值，第几行第几个，索引从0开始
data = table.cell(2,0).value
print (data)


