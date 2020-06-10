# 引入数据库包
import mysql.connector as conn
# 连接数据库
myConnection = conn.connect(host="localhost", user="root", passwd="", database="hqm")
# 创建游标对象(指向服务器端查询结果集合中某个记录位置的变量)
myCursor = myConnection.cursor(dictionary=True)
# 执行sql
sql = "select * from music_user"
myCursor.execute(sql)
result = myCursor.fetchall()
print(result)