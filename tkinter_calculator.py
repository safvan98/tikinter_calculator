from tkinter import *

root = Tk()
root.title("Calculator")
display = Entry(root, width=6, borderwidth=2)
display.grid(row=1, columnspan=6, sticky=W + E)

i = 0


def operation(x):
    global i
    display.insert(i, x)
    i += 1


def all_clear():
    display.delete(0, END)


def back():
    full_element = display.get()
    if len(full_element):
        new_element = full_element[:-1]
        all_clear()
        display.insert(0, new_element)
    else:
        all_clear()
        display.insert(0, "Error")


def functions(x):
    global i
    length = len(x)
    display.insert(i, x)
    i += length


def calculate():
    full_element = display.get()
    try:
        a = eval(full_element)
        all_clear()
        display.insert(0, a)
    except:
        all_clear()
        display.insert(0, "Error")


Button(root, text="1", height=2, width=2, command=lambda: operation(1)).grid(row=2, column=0)
Button(root, text="2", height=2, width=2, command=lambda: operation(2)).grid(row=2, column=1)
Button(root, text="3", height=2, width=2, command=lambda: operation(3)).grid(row=2, column=2)
Button(root, text="4", height=2, width=2, command=lambda: operation(4)).grid(row=3, column=0)
Button(root, text="5", height=2, width=2, command=lambda: operation(5)).grid(row=3, column=1)
Button(root, text="6", height=2, width=2, command=lambda: operation(6)).grid(row=3, column=2)
Button(root, text="7", height=2, width=2, command=lambda: operation(7)).grid(row=4, column=0)
Button(root, text="8", height=2, width=2, command=lambda: operation(8)).grid(row=4, column=1)
Button(root, text="9", height=2, width=2, command=lambda: operation(9)).grid(row=4, column=2)
# Button(root,text="00",height=2,width=2,command=lambda :operation(00)).grid(row=5,column=0)
Button(root, text="0", height=2, width=2, command=lambda: operation(0)).grid(row=5, column=1)
Button(root, text="+", height=2, width=2, command=lambda: functions("+")).grid(row=5, column=3)
Button(root, text="-", height=2, width=2, command=lambda: functions("-")).grid(row=4, column=3)
Button(root, text="(", height=2, width=2, command=lambda: functions("(")).grid(row=3, column=3)
Button(root, text=")", height=2, width=2, command=lambda: functions(")")).grid(row=2, column=3)
Button(root, text="x", height=2, width=2, command=lambda: functions("*")).grid(row=5, column=4)
Button(root, text="/", height=2, width=2, command=lambda: functions("/")).grid(row=4, column=4)
Button(root, text="^", height=2, width=2, command=lambda: functions("**")).grid(row=3, column=4)
Button(root, text="^2", height=2, width=2, command=lambda: functions("**2")).grid(row=2, column=4)
Button(root, text="=", height=2, width=2, command=lambda: calculate()).grid(row=5, column=5)
Button(root, text="!", height=2, width=2).grid(row=4, column=5)
Button(root, text="%", height=2, width=2, command=lambda: functions("%")).grid(row=3, column=5)
Button(root, text="<-", height=2, width=2, command=lambda: back()).grid(row=2, column=5)
Button(root, text="AC", height=2, width=2, command=lambda: all_clear()).grid(row=5, column=6)
Button(root, text=".", height=2, width=2, command=lambda: functions(".")).grid(row=5, column=2)
Button(root, text="pi", height=2, width=2, command=lambda: functions(*3.14)).grid(row=4, column=6)
Button(root, text="exp", height=2, width=2, command=lambda: functions("**")).grid(row=3, column=6)

root.mainloop()
