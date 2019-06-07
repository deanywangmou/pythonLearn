import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='pythonLearn')
curson = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 更改获取数据结果的数据类型,默认是元组,可以改为字典

# sql = "CREATE TABLE IF NOT EXISTS ACCOUNT(id INT, name VARCHAR(20),balance DOUBLE )"
# curson.execute(sql)

try:
    insertSQL0="INSERT INTO ACCOUNT (id,name,balance) VALUES (1,'wangmou',26000),(2,'cherry',16000)"
    insertSQL1="UPDATE account set balance=balance-5000 WHERE name='wangmou'"
    insertSQL2="UPDATE account set balance=balance+5000 WHERE name='cherry'"

    cursor = conn.cursor()

    cursor.execute(insertSQL0)
    conn.commit()

    cursor.execute(insertSQL1)
    raise Exception
    cursor.execute(insertSQL2)
    cursor.close()
    conn.commit()

except Exception as e:

    conn.rollback()
    conn.commit()

curson.close()
conn.close()