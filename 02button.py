from  tkinter import *
root = Tk()


def myclick():
    mylabel = Label(root, text="Look i clicked a button",fg="red")
    mylabel.pack()

myButton = Button(root, text="click me", command=myclick, fg="blue",bg="red")
myButton.pack()
root.mainloop()
