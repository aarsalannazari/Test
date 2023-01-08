from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry('150x100')
window.configure(background='gray')
window.resizable(width=False,height=False)

text=StringVar()
label=Label(window,text variable=text)

button=(window,text='test', command=lambda:text.set('''hello world
I am Amirarsalan
I am 12 years old
I am almost beginner and I love programming
I live in Iran and I am originally Iranian''')).pack()
window.mainloop()
