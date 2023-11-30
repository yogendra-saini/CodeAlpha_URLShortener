import pyshorteners
from tkinter import *

win = Tk()
win.geometry("400x300")
win.configure(bg="white")

def short():
    url = entry1.get()
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    entry2.delete(0, END)
    entry2.insert(END, shortened_url)

l=Label(win, text="URL Link Shortner", font="impack 17 bold",fg="orange")
l.pack(padx=0,pady=10)
entry1 = Entry(win, font='10', bd=3, width=30)
entry1.pack(pady=10)

Button(win, text="Click Me", font="impack 12 bold", bg="#151B54", fg="white", command=short).pack(pady=10)

entry2 = Entry(win, font="impack 16 bold", bg="white", width=24,bd=0)
entry2.pack(pady=30)

win.mainloop()
