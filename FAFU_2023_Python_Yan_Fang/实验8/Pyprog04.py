import pymssql
from openpyxl import Workbook
server = '(local)'
database = 'school'
username = 'sa'
password = '123456'

conn = pymssql.connect(server=server, user=username, password=password, database=database,tds_version="7.0")
cur = conn.cursor()
n=int(input())

sq1='''SELECT student.Sno, student.Sname, course.Cno, course.Cname, SC.Grade
FROM student
JOIN SC ON student.Sno = SC.Sno
JOIN course ON course.Cno = SC.Cno
WHERE SC.Grade > %s'''
cur.execute(sq1,n)
result = cur.fetchall()
wb=Workbook()
ws=wb.active

ws.append(['学号','姓名','课程号','课程名','成绩'])

for row in result:
     ws.append(row)
excelfile=('user.xlsx')
wb.save(excelfile)

cur.close()
conn.close