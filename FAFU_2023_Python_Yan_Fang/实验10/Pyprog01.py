import tkinter as tk
import pymssql
conn=pymssql.connect(host='localhost',user='sa',password='123456',database='school')
win=tk.Tk()
win.title("学生信息查询")
label=tk.Label(win,text="请输入学生姓名:")
label.pack()
entry=tk.Entry(win,width=30)
entry.pack()
def search_student():
    student_name=entry.get()
    cursor=conn.cursor()
    cursor.execute(f"SELECT * FROM student WHERE name LIKE '%{student_name}%'")
    results=cursor.fetchall()
    conn.close()
    text.dedlete(1.0,tk.END)
    for row in results:
        text.insert(tk.END,f"学号：{row[0]} 姓名：{row[1]} 年龄：{row[2]}\n")
button=tk.Button(win,text="查询",command=search_student)
button.pack()
text=tk.Text(win,width=50,height=10)
text.pack()
win.mainloop()
