from tkinter import *
win= Tk()
win.title("This is Justin")
win.geometry('300x200')
a=Label(win,text="justin is great")
a.grid(column=2,row=3)
mytext=Entry(win,width=10)
mytext.grid(column=3,row=1)
def clickme():
    out="you wrote"+mytext.get()
    a.configure(text=out)
btn= Button(win,text='click here', command=clickme,fg="white",bg="purple")
btn.grid(column=2, row=1)
win.mainloop()