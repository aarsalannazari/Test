from tkinter import *
from tkinter import messagebox
def text_message():
	text.set('''hello world
I am Amirarsalan
I am 12 years old
I am almost beginner and I love programming
I live in Iran and I am originally Iranian''')
	messagebox.showinfo('infotmation',text.get())
window=Tk()
window.geometry('150x100')
window.configure(background='gray')
window.resizable(width=False,height=False)

text=StringVar()
label=Label(window,textvariable=text).pack(side=TOP)

button=Button(window,text='test',bd=5,command=lambda:text_message()).pack()
window.mainloop()
