# Importing Modules
from tkinter import *
from math import *
from tkinter import messagebox as msg
# Creation of master Window
master = Tk()
master.title("GUI Based Scientific Calculator V1.0")
icon = PhotoImage(file="t.png")
master.iconphoto(True, icon)
master.resizable(width=FALSE, height=False)
root = Frame(master)
root.config(background="#4D4D4D")
root.grid(padx=5, pady=5)
# Functions
# This Function will clear one character (numbers + operations) in the entry box


def clronce():
    global eq
    calculation.delete(len(calculation.get())-1, END)
    eq = calculation.get()
    # equation.set(eq)
# this function is to insert character (numbers + operations) in the entry box


def btnPress(num):
    global eq
    eq = eq + str(num)
    equation.set(eq)
# this function is for evaluating the expression in the entry box


def equals():
    global eq
    x = calculation.get()
    if eq == "":
        eq = eq + x
    try:
        total = str(eval(eq))
        equation.set(total)
        if float(total) == 0:
            eq = ""
        else:
            eq = total
    except:
        equation.set("ERROR")
        eq = ''
# this function will clear the entire entry box


def Clr():
    global eq
    eq = ""
    equation.set("")
# this function is to generate the difference of two lists (made this for theme)


def dif(l1, l2):
    return [i for i in l1+l2 if i not in l1 or i not in l2]


# Entry Box
eq = ""
equation = StringVar()
calculation = Entry(root, textvariable=equation, font="helvetica 20 bold",
                    width=25, justify=RIGHT, bg='black', fg='#00ff00', bd=15)
calculation.grid(row=0, column=0, columnspan=4)
# Regular Buttons
but1 = Button(root, text='1', command=lambda: btnPress(
    1), font="helvetica 15 bold", width=7, height=2, bg='#1A1A1A', fg='white')
but1.grid(row=1, column=0, pady=3)
but2 = Button(root, text='2', command=lambda: btnPress(
    2), font="helvetica 15 bold", width=7, height=2, bg='#1A1A1A', fg='white')
but2.grid(row=1, column=1, pady=3)
but3 = Button(root, text='3', command=lambda: btnPress(
    3), font="helvetica 15 bold", width=7, height=2, bg='#1A1A1A', fg='white')
but3.grid(row=1, column=2, pady=3)
plus = Button(root, text='+', command=lambda: btnPress("+"),
              font="helvetica 15 bold", width=7, height=2, bg='black', fg='#00ff00',)
plus.grid(row=1, column=3, pady=3)
but4 = Button(root, text='4', command=lambda: btnPress(
    4), font="helvetica 15 bold", width=7, height=2, bg='#1A1A1A', fg='white')
but4.grid(row=2, column=0, pady=3)
but5 = Button(root, text='5', command=lambda: btnPress(
    5), font="helvetica 15 bold", width=7, height=2, bg='#1A1A1A', fg='white')
but5.grid(row=2, column=1, pady=3)
but6 = Button(root, text='6', command=lambda: btnPress(
    6), font="helvetica 15 bold", width=7, height=2, bg='#1A1A1A', fg='white')
but6.grid(row=2, column=2, pady=3)
minus = Button(root, text='-', command=lambda: btnPress("-"),
               font="helvetica 15 bold", width=7, height=2, bg='black', fg='#00ff00',)
minus.grid(row=2, column=3, pady=3)
but7 = Button(root, text='7', command=lambda: btnPress(
    7), font="helvetica 15 bold", width=7, height=2, bg='#1A1A1A', fg='white')
but7.grid(row=3, column=0, pady=3)
but8 = Button(root, text='8', command=lambda: btnPress(
    8), font="helvetica 15 bold", width=7, height=2, bg='#1A1A1A', fg='white')
but8.grid(row=3, column=1, pady=3)

but9 = Button(root, text='9', command=lambda: btnPress(
    9), font="helvetica 15 bold", width=7, height=2, bg='#1A1A1A', fg='white')
but9.grid(row=3, column=2, pady=3)
mul = Button(root, text='*', command=lambda: btnPress("*"),
             font="helvetica 15 bold", width=7, height=2, bg='black', fg='#00ff00',)
mul.grid(row=3, column=3, pady=3)
lb = Button(root, text='(', command=lambda: btnPress(
    "("), font="helvetica 15 bold", width=7, height=2, bg='#1A1A1A', fg='white')
lb.grid(row=4, column=0, pady=3)
zer = Button(root, text='0', command=lambda: btnPress(
    0), font="helvetica 15 bold", width=7, height=2, bg='#1A1A1A', fg='white')
zer.grid(row=4, column=1, pady=3)
rb = Button(root, text=')', command=lambda: btnPress(
    ")"), font="helvetica 15 bold", width=7, height=2, bg='#1A1A1A', fg='white')
rb.grid(row=4, column=2, pady=3)
rem = Button(root, text="←", command=clronce, font="helvetica 15 bold",
             width=7, height=2, bg='black', fg='#00ff00',)
rem.grid(row=5, column=3, pady=3)
clr = Button(root, text='CLEAR', command=Clr, font="helvetica 15 bold",
             width=7, height=2, bg='black', fg='#00ff00',)
clr.grid(row=5, column=0, pady=3)
eql = Button(root, text='=', command=equals, font="helvetica 15 bold",
             width=7, height=2, bg='black', fg='#00ff00',)
eql.grid(row=5, column=1, pady=3)
dot = Button(root, text='.', command=lambda: btnPress(
    "."), font="helvetica 15 bold", width=7, height=2, bg='black', fg='#00ff00',)
dot.grid(row=5, column=2, pady=3)
div = Button(root, text='/', command=lambda: btnPress("/"),
             font="helvetica 15 bold", width=7, height=2, bg='black', fg='#00ff00',)
div.grid(row=4, column=3, pady=3)
# Creating lists of buttons for switching between Themes
numbtn = [but1, but2, but3, but4, but5, but6, but7, but8, but9, lb, zer, rb]
ops = [plus, minus, mul, div, rem, clr, dot, eql]


# Science Buttons

bpi = Button(root, text="π", command=lambda: btnPress(
    "pi"), font="helvetica 15 bold", width=7, height=2, bg='black', fg='#00ff00',)

bsin = Button(root, text="sin", command=lambda: btnPress(
    "sin("), font="helvetica 15 bold", width=7, height=2, bg='black', fg='#00ff00',)

bcos = Button(root, text="cos", command=lambda: btnPress(
    "cos("), font="helvetica 15 bold", width=7, height=2, bg='black', fg='#00ff00',)

btan = Button(root, text="tan", command=lambda: btnPress(
    "tan("), font="helvetica 15 bold", width=7, height=2, bg='black', fg='#00ff00',)

blog = Button(root, text="log", command=lambda: btnPress(
    "log("), font="helvetica 15 bold", width=7, height=2, bg='black', fg='#00ff00',)

bsinh = Button(root, text="sinh", command=lambda: btnPress(
    "sinh("), font="helvetica 15 bold", width=7, height=2, bg='#1A1A1A', fg='white',)

bcosh = Button(root, text="cosh", command=lambda: btnPress(
    "cosh("), font="helvetica 15 bold", width=7, height=2, bg='#1A1A1A', fg='white',)

btanh = Button(root, text="tanh", command=lambda: btnPress(
    "tanh("), font="helvetica 15 bold", width=7, height=2, bg='#1A1A1A', fg='white',)

blog2 = Button(root, text="log2", command=lambda: btnPress(
    "log2("), font="helvetica 15 bold", width=7, height=2, bg='black', fg='#00ff00',)

blog10 = Button(root, text="log10", command=lambda: btnPress(
    "log10("), font="helvetica 15 bold", width=7, height=2, bg='#1A1A1A', fg='white',)

fact = Button(root, text="factorial", command=lambda: btnPress(
    "factorial("), font="helvetica 15 bold", width=7, height=2, bg='#1A1A1A', fg='white',)

babs = Button(root, text="abs", command=lambda: btnPress(
    "abs("), font="helvetica 15 bold", width=7, height=2, bg='#1A1A1A', fg='white',)

rad = Button(root, text="radians", command=lambda: btnPress(
    "radians("), font="helvetica 15 bold", width=7, height=2, bg='black', fg='#00ff00',)

basin = Button(root, text="asin", command=lambda: btnPress(
    "asin("), font="helvetica 15 bold", width=7, height=2, bg='#1A1A1A', fg='white',)

bacos = Button(root, text="acos", command=lambda: btnPress(
    "acos("), font="helvetica 15 bold", width=7, height=2, bg='#1A1A1A', fg='white',)

batan = Button(root, text="atan", command=lambda: btnPress(
    "atan("), font="helvetica 15 bold", width=7, height=2, bg='#1A1A1A', fg='white',)

deg = Button(root, text="degrees", command=lambda: btnPress(
    "degrees("), font="helvetica 15 bold", width=7, height=2, bg='black', fg='#00ff00',)

be = Button(root, text="e", command=lambda: btnPress(
    "e"), font="helvetica 15 bold", width=7, height=2, bg='black', fg='#00ff00',)

sqr = Button(root, text="√", command=lambda: btnPress(
    "sqrt("), font="helvetica 15 bold", width=7, height=2, bg='black', fg='#00ff00',)

exp = Button(root, text="round", command=lambda: btnPress(
    "round("), font="helvetica 15 bold", width=7, height=2, bg='black', fg='#00ff00',)
scibtn = [bpi, bsin, bcos, btan, blog, bsinh, bcosh, btanh, blog2,
          blog10, fact, babs, rad, basin, bacos, batan, deg, be, sqr, exp]
ops.extend([bpi, bsin, bcos, btan, blog, blog2, rad, deg, be, sqr, exp])
numbtn.extend(dif(scibtn, ops))
# Menus and functions

# Function for exit


def iExit():
    if msg.askyesno("Scientific Calculator", 'Do You Really Want to Quit ?'):
        master.destroy()
        return


# function for standard mode
def standard():
    for i in scibtn:
        i.grid_forget()

# function for scientific mode


def scientific():
    rw = 1
    cl = 4
    for i in scibtn:
        i.grid(row=rw, column=cl, pady=3, padx=4)
        cl += 1
        if cl > 7:
            cl = 4
            rw += 1

# function for Light Theme


def light():
    root.config(background="#A45E4D")
    calculation.config(bg='#FFF8AF', fg='black')
    for i in numbtn:
        i.config(bg='#FDD1A1', fg='black')
    for i in ops:
        i.config(bg='#FFF8AF', fg='black')

# function for Dark Theme


def dark():
    root.config(background="#4D4D4D")
    calculation.config(bg='black', fg='#00ff00')
    for i in numbtn:
        i.config(bg='#1A1A1A', fg='white')
    for i in ops:
        i.config(bg='black', fg='#00ff00')


# Creating menubar
menubar = Menu(root)
modemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Modes', menu=modemenu)
modemenu.add_command(label='Standard', command=standard)
modemenu.add_command(label='Scientific', command=scientific)
modemenu.add_separator()
modemenu.add_command(label='Exit', command=iExit)

thememenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Themes', menu=thememenu)
thememenu.add_command(label='Dark', command=dark)
thememenu.add_command(label='Light', command=light)

master.config(menu=menubar)

# executing
master.mainloop()
