import tkinter as tk
from tkinter import filedialog
def open_file():
    file_path=filedialog.askopenfilename(title='打开文件',filetypes=[('文本文件','*.txt'),('所有文件','*')])
    if file_path:
        with open(file_path,'r') as file:
            content=file.read()
            text_widget.delete(1.0,tk.END)
            text_widget.insert(tk.END,content)
def save_file():
    file_path=filedialog.asksaveasfilename(title='保存文件',defaultextension='.txt',filetypes=[('文本文件','*.txt'),('所有文件','*')])
    if file_path:
        content=text_widget.get(1.0,tk.END)
        with open(file_path,'w') as file:
            file.write(content)
def exit_app():
    root.destroy()

root=tk.Tk()
root.title('文件操作')
text_widget=tk.Text(root,wrap=tk.WORD)
text_widget.pack()
open_button = tk.Button(root,text='打开',command=open_file)
open_button.pack(side=tk.LEFT)
save_button=tk.Button(root,text='保存',command=save_file)
save_button.pack(side=tk.LEFT)
exit_button=tk.Button(root,text='退出',command=exit_app)
exit_button.pack(side=tk.LEFT)
root.mainloop()
