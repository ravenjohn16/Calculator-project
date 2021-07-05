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
