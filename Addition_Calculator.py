from tkinter import *


def Calculator_add():
    text = entry.get()
    num1 = int(text)
    text1 = entry1.get()
    num2 = int(text1)
    label1['text'] = (num1,'+',num2,'=')
    label['text'] = num1 + num2


root = Tk()
root.title('Simple Calculator')

entry = Entry(root)
entry.grid(row=1, column=1)
entry1 = Entry(root)
entry1.grid(row=2, column=1)

button = Button(root, text="Add Numbers", command=Calculator_add)
button.grid(row=3, column=1)

Label(root, text="Number One").grid(row=1)
Label(root, text="Number Two").grid(row=2)

label = Label(root)
label.grid(row=5, column=1)
label1 = Label(root)
label1.grid(row=4, column=1)


root.mainloop()
