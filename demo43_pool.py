# py中使用mysql-connector来完成连接池管理
import mysql.connector.pooling as pooling
pool = pooling.MySQLConnectionPool(
    pool_size=5,
    host="localhost",
    user="root",
    passwd="",
    database="xz"
) 
myConnection = pool.get_connection()
myCursor = myConnection.cursor(dictionary=True)
sql = "select * from xz_user"
myCursor.execute(sql)
result = myCursor.fetchall()
print(result)