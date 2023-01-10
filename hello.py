from tkinter import *
from tkinter import messagebox
def text_message_e():
	text.set('''hello world
I am Amirarsalan
I am 12 years old
I am almost beginner and I love programming
I live in Iran and I am originally Iranian''')
	messagebox.showinfo('infotmation',text.get())
def text_message_f():
	text.set('''سلام مردم دنیا
من امیر ارسلان هستم
من دوازده سال دارم
من تقریبا مبتدی هستم اما دانشم از مبتدی یکم بالا تره
من تو ایران زندگی میکنم و اصالتا هم ایرانی هستم''')
	messagebox.showinfo('اطلاعات',text.get())
window=Tk()
window.title('introducing')
window.geometry('350x300')
window.configure(background='gray')
window.resizable(width=False,height=False)

text=StringVar()
label=Label(window,textvariable=text).pack(side=TOP)

button=Button(window,text='test',bd=5,command=lambda:text_message_e()).pack()
button=Button(window,text='تست',bd=5,command=lambda:text_message_f()).pack()
window.mainloop()
