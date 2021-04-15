# -*-  coding：utf-8  -*-
import  xlrd
import  time
xl = xlrd.open_workbook(r'vcard2.xls')
wl=open('vcard20.vcf', 'w', encoding='utf8')

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
# col = table.col_values(0)
# print ('获取第一列的整列的内容',col)

# def  getTimeStamp3():
#     prentTime=time.time()*1000
#     prentTimeSplit=str(prentTime).split(".")
#     return  prentTimeSplit[0]
# print (getTimeStamp3())
num=11749496800
for i in range(rows):
    # num=11749496800
    def getTimeStamp3():
        prentTime = time.time() * 1000
        prentTimeSplit = str(prentTime).split(".")
        return prentTimeSplit[0]
    one='BEGIN:VCARD'+'\n'
    two='UID:'+str(num)+'\n'
    nrow=table.row_values(i) #获取每行内容
    nrow1=nrow[0]
    nrow2=int(nrow[1])
    three ='N:;'+nrow1+';;;'+'\n'
    four='EMAIL;type=INTERNET;type=pref:'+str(nrow2)+'@qq.com'+'\n'
    five='TEL;type=CELL;type=VOICE;type=pref:'+str(nrow2)+'\n'
    six='FN:'+nrow1+'\n'
    timeNow = getTimeStamp3()+'\n'
    seven='REV:'+timeNow
    eight='CID:'+str(num)+'\n'
    ten='VERSION:3.0\n'
    elevec='END:VCARD\n'
    print (one,two,three,four,five,six,seven,eight,ten,elevec)

    wl.write(one)
    wl.write(two)
    wl.write(three)
    wl.write(four)
    wl.write(five)
    wl.write(six)
    wl.write(seven)
    wl.write(eight)
    wl.write(ten)
    wl.write(elevec)
    num = num + 1
    time.sleep(0.01)

wl.close()



