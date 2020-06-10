# 引入数据库包
import mysql.connector as conn
# 连接数据库
myConnection = conn.connect(host="localhost", user="root", passwd="", database="music")
# 创建游标对象(指向服务器端查询结果集合中某个记录位置的变量)
myCursor = myConnection.cursor(dictionary=True)
# 执行sql
sql = "select * from music_user limit %s,%s"
myCursor.execute(sql, (1,1))
# sql = "insert into music_user (name, password) values ('joker', '123456')"
# myCursor.execute(sql)
# myConnection.commit()
# myCursor.rowcount   受影响行数
# myCursor.lastrowid  最后操作id
result = myCursor.fetchall()
print(result)