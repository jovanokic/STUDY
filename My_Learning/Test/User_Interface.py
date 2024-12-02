from tkinter import *

root = Tk()

root1 = Tk()

#Creating the thing
my_label = Label(root, text = "test_label")
my_label1 = Label(root, text = "test_label1")
my_label2 = Label(root, text = "test_label2")

#Putting it on the screen
my_label.grid(row=0, column=0)
my_label1.grid(row=1, column=0)
my_label2.grid(row=2, column=0)


root.mainloop()
