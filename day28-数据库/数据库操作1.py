import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='pythonLearn')
curson = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 更改获取数据结果的数据类型,默认是元组,可以改为字典
# curson = conn.cursor()  # 更改获取数据结果的数据类型,默认是元组,可以改为字典

sql = "CREATE TABLE IF NOT EXISTS EMPLOYEE(id INT, name VARCHAR(20))"
curson.execute(sql)


# insertSql="INSERT INTO EMPLOYEE VALUES (5,'wangmou'),(6,'deany')"
#
# ret=curson.execute(insertSql)
# print(ret)    # 2

ret=curson.execute("SELECT  * FROM  EMPLOYEE")
print(ret)

# print(curson.fetchone())
# print(curson.fetchone())
# # print(curson.fetchall())
#
# curson.scroll(-1,mode='relative')  # 相对当前位置移动,-1向上移，1向下移
# print(curson.fetchone())
# curson.scroll(2,mode='absolute') # 相对绝对位置移动
# print(curson.fetchone())
print(curson.fetchmany(3))

conn.commit()  # 插入语句必须要commit
curson.close()
conn.close()
