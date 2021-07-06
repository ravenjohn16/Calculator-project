# Imports
from tkinter import *
from tkinter import messagebox
from brains import *

# Colors
BG           = "#3A383B" # For True Background
ORANGE       = "#FFA00B" # For Operation Symbols
DARK_GRAY    = "#464543" # For clear, del, and pi
LIGHT_GRAY   = "#646462" # For Numerics
TEXT_BUTTONS = "#E7E5E4" # For font color of buttons
TEXT_INPUT   = "#FFFFFF" # For font color in the input (Entry widget)
BOTTOM_OUT_1 = "#A2A2A1" # DARK_GRAY <- Used when key is pressed
BOTTOM_OUT_2 = "#B1B1B0" # LIGHT_GRAY <- Used when key is pressed
BOTTOM_OUT_3 = "#FFCF85" # ORANGE <- Used when key is pressed

# Formats
f1 = ('Helvetica', 25, 'bold') # Setting of font for clear, del, and pi
f2 = ('Helvetica', 30)         # Setting of font for numbers
f3 = ('Helvetica', 50)         # Setting of font for operation symbols
f4 = ('Helvetica', 45, 'bold') # Setting of font for output screen
f5 = ('Helvatica', 40)         # Setting of font for result screen

# Header
root = Tk()
root.geometry('500x600')
root.title('Calculator')
#root.iconbitmap('images/logo.ico')
root.configure(background=BG)

# vars
# def update():
#     db = str(dS.get_data())

#     dr = str(dS.get_result())

# Row Configure
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=5)
root.rowconfigure(3, weight=5)
root.rowconfigure(4, weight=5)
root.rowconfigure(5, weight=5)
root.rowconfigure(6, weight=5)

# Column Configure
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

# Vars
dr = StringVar() # Upper box
dr.set(dS.get_data)
db = StringVar() # Lower box
db.set(dS.get_result)

# Output screen
e_screen   = Entry(root, font=f4, bg=BG, fg=TEXT_INPUT, justify=RIGHT, cursor='arrow', textvariable=dr, relief=FLAT, state=DISABLED, disabledbackground=BG, disabledforeground=TEXT_INPUT).grid(row=0, column=0, columnspan=4, sticky='nsew')
e_result   = Entry(root, font=f5, bg=BG, fg=TEXT_INPUT, justify=RIGHT, cursor='arrow', textvariable=db, relief=FLAT, state=DISABLED, disabledbackground=BG, disabledforeground=TEXT_INPUT).grid(row=1, column=0, columnspan=4, sticky='nsew')

# Buttons
b_clear    = Button(root, command= lambda: cls(), text='AC', font=f1, bg=DARK_GRAY, activebackground=BOTTOM_OUT_1, fg=TEXT_BUTTONS, relief=FLAT)
b_del      = Button(root, command= lambda: dels(), text='←', font=f1, bg=DARK_GRAY, activebackground=BOTTOM_OUT_1, fg=TEXT_BUTTONS, relief=FLAT)
b_pi       = Button(root, command= lambda: press('π'), text='π', font=f1, bg=DARK_GRAY, activebackground=BOTTOM_OUT_1, fg=TEXT_BUTTONS, relief=FLAT)
b_divide   = Button(root, command= lambda: press('/'), text='÷', font=f3, bg=ORANGE, activebackground=BOTTOM_OUT_3, fg=TEXT_BUTTONS, relief=FLAT)

b_seven    = Button(root, command= lambda: press('7'), text='7', font=f2, bg=LIGHT_GRAY, activebackground=BOTTOM_OUT_2, fg=TEXT_BUTTONS, relief=FLAT)
b_eight    = Button(root, command= lambda: press('8'), text='8', font=f2, bg=LIGHT_GRAY, activebackground=BOTTOM_OUT_2, fg=TEXT_BUTTONS, relief=FLAT)
b_nine     = Button(root, command= lambda: press('9'), text='9', font=f2, bg=LIGHT_GRAY, activebackground=BOTTOM_OUT_2, fg=TEXT_BUTTONS, relief=FLAT)
b_multiply = Button(root, command= lambda: press('*'), text='×', font=f3, bg=ORANGE, activebackground=BOTTOM_OUT_3, fg=TEXT_BUTTONS, relief=FLAT)

b_four     = Button(root, command= lambda: press('4'), text='4', font=f2, bg=LIGHT_GRAY, activebackground=BOTTOM_OUT_2, fg=TEXT_BUTTONS, relief=FLAT)
b_five     = Button(root, command= lambda: press('5'), text='5', font=f2, bg=LIGHT_GRAY, activebackground=BOTTOM_OUT_2, fg=TEXT_BUTTONS, relief=FLAT)
b_six      = Button(root, command= lambda: press('6'), text='6', font=f2, bg=LIGHT_GRAY, activebackground=BOTTOM_OUT_2, fg=TEXT_BUTTONS, relief=FLAT)
b_minus    = Button(root, command= lambda: press('-'), text='-', font=f3, bg=ORANGE, activebackground=BOTTOM_OUT_3, fg=TEXT_BUTTONS, relief=FLAT)

b_one      = Button(root, command= lambda: press('1'), text='1', font=f2, bg=LIGHT_GRAY, activebackground=BOTTOM_OUT_2, fg=TEXT_BUTTONS, relief=FLAT)
b_two      = Button(root, command= lambda: press('2'), text='2', font=f2, bg=LIGHT_GRAY, activebackground=BOTTOM_OUT_2, fg=TEXT_BUTTONS, relief=FLAT)
b_three    = Button(root, command= lambda: press('3'), text='3', font=f2, bg=LIGHT_GRAY, activebackground=BOTTOM_OUT_2, fg=TEXT_BUTTONS, relief=FLAT)
b_plus     = Button(root, command= lambda: press('+'), text='+', font=f3, bg=ORANGE, activebackground=BOTTOM_OUT_3, fg=TEXT_BUTTONS, relief=FLAT)

b_zero     = Button(root, command= lambda: press('0'), text='0', font=f2, bg=LIGHT_GRAY, activebackground=BOTTOM_OUT_2, fg=TEXT_BUTTONS, relief=FLAT)
b_decimal  = Button(root, command= lambda: press('.'), text='.', font=f1, bg=LIGHT_GRAY, activebackground=BOTTOM_OUT_2, fg=TEXT_BUTTONS, relief=FLAT)
b_equals   = Button(root, command= lambda: equals(), text='=', font=f3, bg=ORANGE, activebackground=BOTTOM_OUT_3, fg=TEXT_BUTTONS, relief=FLAT)

# Button gridding
b_clear.grid(row=2, column=0, sticky='nsew')
b_del.grid(row=2, column=1, sticky='nsew')
b_pi.grid(row=2, column=2, sticky='nsew')
b_divide.grid(row=2, column=3, sticky='nsew')   ##

b_seven.grid(row=3, column=0, sticky='nsew')
b_eight.grid(row=3, column=1, sticky='nsew')
b_nine.grid(row=3, column=2, sticky='nsew')
b_multiply.grid(row=3, column=3, sticky='nsew') ##

b_four.grid(row=4, column=0, sticky='nsew')
b_five.grid(row=4, column=1, sticky='nsew')
b_six.grid(row=4, column=2, sticky='nsew')
b_minus.grid(row=4, column=3, sticky='nsew')    ##

b_one.grid(row=5, column=0, sticky='nsew')
b_two.grid(row=5, column=1, sticky='nsew')
b_three.grid(row=5, column=2, sticky='nsew')
b_plus.grid(row=5, column=3, sticky='nsew')     ##

b_zero.grid(row=6, column=0, columnspan=2, sticky='nsew')
b_decimal.grid(row=6, column=2, sticky='nsew')
b_equals.grid(row=6, column=3, sticky='nsew')   ##

def updateEntries():
    temp  = str(dS.get_data())
    resulta = str(dS.get_result())
    preliminarya = temp.replace('*', '×').replace('/', '÷')
    dr.set(preliminarya)
    db.set(resulta)
    root.after(10, updateEntries)

def runThis(self):
    messagebox.showinfo("Notice", "Result copied to clipboard")
    copy2Clip()
    
# Detecting key presses
root.bind('<Key>', key_press)
root.bind('<Return>', runThis)
# $Important
root.after(10, updateEntries)
root.mainloop()
