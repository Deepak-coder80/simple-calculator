# THIS CODE BY DEEPAK M S


from tkinter import *

window = Tk()
# Heading for the calculator
window.title("CALCULATOR")
# Input window of calculator
e = Entry(window, width=50, borderwidth=5, relief=RIDGE, fg="Green", bg="white")
e.grid(row=0, columnspan=4, padx=10, pady=15)


# function for adding numbers to the calculator screen
def click(to_print):
    old = e.get()
    e.delete(0, END)
    e.insert(0, old + to_print)
    return


# function for clearing the screen
def clear():
    e.delete(0, END)
    return


# function for backspace
def bksp():
    current = e.get()
    length = len(current) - 1
    e.delete(length, END)


# function for evaluating the operations
def evaluate():
    ans = e.get()
    ans = eval(ans)
    e.delete(0, END)
    e.insert(0, ans)


# keys in first row
plus = Button(window, text="+", padx=29, pady=10, bg="black", fg="white", command=lambda: click("+"))
diff = Button(window, text="-", padx=29, pady=10, bg="black", fg="white", command=lambda: click("-"))
bkspace = Button(window, text="<--", padx=29, pady=10, bg="lightgreen", fg="Black", command=lambda: bksp())
clr = Button(window, text="AC", padx=29, pady=10, bg="Red", fg="Black", command=lambda: clear())

# keys in second row
seve = Button(window, text="7", padx=29, pady=10, bg="gray", fg="Black", command=lambda: click("7"))
eigh = Button(window, text="8", padx=29, pady=10, bg="gray", fg="Black", command=lambda: click("8"))
nine = Button(window, text="9", padx=29, pady=10, bg="gray", fg="Black", command=lambda: click("9"))
mult = Button(window, text="*", padx=29, pady=10, bg="black", fg="white", command=lambda: click("*"))

# keys in 3rd row
four = Button(window, text="4", padx=29, pady=10, bg="gray", fg="Black", command=lambda: click("4"))
five = Button(window, text="5", padx=29, pady=10, bg="gray", fg="Black", command=lambda: click("5"))
sixb = Button(window, text="6", padx=29, pady=10, bg="gray", fg="Black", command=lambda: click("6"))
divd = Button(window, text="/", padx=29, pady=10, bg="black", fg="white", command=lambda: click("/"))

# keys in 4th row
oneb = Button(window, text="1", padx=29, pady=10, bg="gray", fg="Black", command=lambda: click("1"))
twob = Button(window, text="2", padx=29, pady=10, bg="gray", fg="Black", command=lambda: click("2"))
thre = Button(window, text="3", padx=29, pady=10, bg="gray", fg="Black", command=lambda: click("3"))
equl = Button(window, text="=", padx=29, pady=10, bg="green", fg="white", command=lambda: evaluate())

# key grids in first row
plus.grid(row=1, column=0)
diff.grid(row=1, column=1)
bkspace.grid(row=1, column=2)
clr.grid(row=1, column=3)

# key grids in second row
seve.grid(row=2, column=0)
eigh.grid(row=2, column=1)
nine.grid(row=2, column=2)
mult.grid(row=2, column=3)

# key grids in 3rd row
four.grid(row=3, column=0)
five.grid(row=3, column=1)
sixb.grid(row=3, column=2)
divd.grid(row=3, column=3)

# key grids in 4th row
oneb.grid(row=4, column=0)
twob.grid(row=4, column=1)
thre.grid(row=4, column=2)
equl.grid(row=4, column=3)

window.mainloop()
