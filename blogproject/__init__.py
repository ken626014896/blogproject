import pymysql

pymysql.install_as_MySQLdb()


db=pymysql.connect("localhost","root","123456","blogproject_db")


cursor=db.cursor()

cursor.execute("SELECT VERSION()")

data=cursor.fetchone()

print("Datebase  version is :%s"%  data)


db.close()