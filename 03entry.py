from  tkinter import *
root = Tk()
e = Entry(root, width=50,fg="white",bg="blue",borderwidth=5)
e.pack()
e.insert(0, "Enter your name")


def myclick():
    mylabel = Label(root, text="hello " + e.get(),fg="red")
    mylabel.pack()

myButton = Button(root, text="click me", command=myclick, fg="blue",bg="red")
myButton.pack()
root.mainloop()
