import tkinter
from tkinter import messagebox
def login():
    user=enu.get()
    pswd=enp.get()
    if not user:
        messagebox.showwarning(title=None,message='用户名不能为空！')
    elif not pswd:
        messagebox.showwarning(title=None,message='密码不能为空！')
    else:
        print(f"用户名：{user}")
        print(f"密码：{pswd}")
def close():
    window.destroy()
window=tkinter.Tk()
window.title("输入框界面")
window.geometry ("400x200")
lu=tkinter.Label(window,text="用户名")
lu.pack()
enu=tkinter.Entry(window)
enu.pack()
lp=tkinter.Label(window,text="密码")
lp.pack()
enp=tkinter.Entry(window,show="●")
enp.pack()
btnl=tkinter.Button(window,text="登录",command=login)
btnl.pack()
btne=tkinter.Button(window,text="退出",command=close)
btne.pack()
window.mainloop()
