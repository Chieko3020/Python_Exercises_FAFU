import pymssql

server = '(local)'
database = 'school'
username = 'sa'
password = '123456'

conn = pymssql.connect(server=server, user=username, password=password, database=database,tds_version="7.0")
cur = conn.cursor()
try:
    sq1='create table course(Cno varchar(20) primary key,Cname varchar(255) not null,Credit int not null)'

    cur.execute(sq1)

    while True:
        data=tuple(input().split(' '))
        if data[0]=='q':
            break
        sq2='insert into course(Cno,Cname,Credit) values(%s,%s,%s)'
        cur.execute(sq2,data)
        conn.commit()
    sq3='select Cno,Cname from course'
    cur.execute(sq3)
    courses=cur.fetchall()

    for course in courses:
        print(f'{course[0],course[1]}')

    cur.close()
    conn.close()
except:
    print('数据输入有误!')
