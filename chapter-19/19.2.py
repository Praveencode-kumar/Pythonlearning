
#Exercise 19.2
from tkinter import *
from tkinter import Canvas

top = Tk()
top.geometry("300x250")
def circleWindow():
    C = Canvas(top,bg='blue', height=250, width=300)
    oval = C.create_oval(70, 30, 200, 200, fill="Red")
    C.pack()
b = Button(top, text= "Click me for Graph", command = circleWindow)
b.place(x=90,y=100)
top.mainloop()

