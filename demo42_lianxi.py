uname = input("请输入用户名：")
upwd = input("请输入密码：")

import mysql.connector as con
myConnection = con.connect(host="localhost",user="root",passwd="",database="xz")
myCursor = myConnection.cursor(dictionary=True)
sql = "insert into xz_user (uname, upwd) values(%s, %s)"
myCursor.execute(sql, (uname,upwd))
myConnection.commit()
print(myCursor.rowcount, myCursor.lastrowid)