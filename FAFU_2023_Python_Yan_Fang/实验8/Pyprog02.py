import pymssql

server = '(local)'
database = 'school'
username = 'sa'
password = '123456'

conn = pymssql.connect(server=server, user=username, password=password, database=database,tds_version="7.0")
cur = conn.cursor()
age=tuple(input().split())
sql='select * from student where Sname= %s or Ssex= %s'
cur.execute(sql,age)
temp=0
rows=cur.fetchall()
for i in rows:
    print(i)
    temp=temp+i[-1]
print(temp/len(rows))

conn.close()
