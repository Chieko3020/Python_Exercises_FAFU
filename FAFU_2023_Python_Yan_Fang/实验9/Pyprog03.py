import tkinter as tk
def click ( event):
    if ( event . widget ['text'] in ('0','1','2','3','4','5','6','7','8','9','.')):
        if show ['text']=='' and event . widget ['text']=='0':
            pass
        else :
            show ['text']= show ['text']+event . widget ['text']
    elif ( event . widget ['text']in ('+','-','*','/','%','**','//')):
            show ['text']= show ['text']+ event . widget ['text']
    elif( event . widget ['text']=='=' and  show ['text'] is not None):
            lbText= show ['text']
            try:
                show ['text']= str ( eval ( lbText ))
            except:
                show ['text']="0"            
            finally:               
                lbText= None
        
def clean ( event):
################
      show['text']=""                                        #【1】清空标签显示的内容


######===========
     
master= tk.Tk ()
master .title ("简单科学计算器")
show = tk.Label ( relief = tk.SUNKEN, font =('Courier New',24), width =23, bg ='white', anchor = "e")
show. pack ( side = tk.TOP , pady =10)
p= tk.Frame ( master )
p . pack ( side = tk.TOP)
names=("+","1","2","3","С","-","4","5","6","**","*","7","8","9","//","/",".","0","%","=")
######===========================
for i in range (len ( names)):
       b=tk.Button(p,text=names[i],font=('Verdana',20),width=5)    #【2】创建Button向量b,将其放入p框架中，文本为name[i],字体为('Verdana',20)，宽度为5；
       b . grid (row = i //5, column = i %5)
       b.bind("<Button-1>",click)                                                          #【3】为鼠标左键的双击事件绑定click方法
       if names[i]=='C':
           b.bind("Double-1",clean)# 【4】当按钮的字符为C时，为鼠标左键的双击事件绑定clean方法

master.mainloop()                    #【5】主窗口开启消息循环
######===========================
