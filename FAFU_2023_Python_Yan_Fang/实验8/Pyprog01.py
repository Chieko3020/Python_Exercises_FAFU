import pymssql
try:
    conn = pymssql.connect(host='localhost',user='sa',password='123456',database='school',charset='GBK')
    cur=conn.cursor()
    n=int(input())
    mysql = "select top %s * from student"
    cur.execute(mysql,n)
except:
    print("连接和操作数据库有误")
results = cur.fetchall()
for row in results:
    print(row)
cur.close()
conn.close()
