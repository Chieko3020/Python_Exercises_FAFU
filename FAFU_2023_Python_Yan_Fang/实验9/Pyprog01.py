import tkinter

def change():
    lb.config(bg=color[int(var.get())])  

window=tkinter.Tk()
window.title ("改变颜色")
window.geometry ("400x200")
lb=tkinter.Label(window,bg="red",width=60,height=2)
lb.grid(row=0, column=0,columnspan=2) 
var=tkinter.StringVar(value=0)
color=['red','blue','yellow']
for n in range (len(color)):    
     btn=tkinter.Radiobutton(window,variable=var,text=color[n],value=n,command=change)
     btn.grid(row=n+1,column=0,sticky='w')
window.mainloop()

 
