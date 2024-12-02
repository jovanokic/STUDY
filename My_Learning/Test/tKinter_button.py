from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Just a regular Button")
    myLabel.pack()

my_button = Button(root,text="Click Me!", padx=25, pady=12.5, command=myClick)
my_button.pack()

root.mainloop()