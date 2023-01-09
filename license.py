from tkinter import *
from tkinter import messagebox
def license_e():
	data.set("""please don't clone my projects and edit
if you want to save my project and edit please fork them """)
	messagebox.showinfo('license',data.get())
def license_f():
	data.set("""اگر میخواهید برنامه را ذخیره کنید دکمه fork را فشار دهید """)
	messagebox.showinfo('مجوز',data.get())
window=Tk()
window.title('license')
window.geometry('150x150')
data=StringVar()
button_e=Button(window,text='license',bd=6,command=lambda:license_e(),justify='center').grid(row=0,column=0)
button_f=Button(window,text='مجوز',bd=6,command=lambda:license_f(),justify='center').grid(row=0,column=1)
window.mainloop()
