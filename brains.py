from math import pi
import subprocess
from tkinter.constants import TRUE # Used in copy to clipboard function

# Storing of data in private, $Used a constructor with setter and getter to avoid global variables
class DataStorage:
    # Constructor
    def __init__(self):
        self._data = "0"
        self._result = "0"
        
    # Getter
    def get_data(self):
        return self._data
    # Setter
    def set_data(self, inputs):
        self._data = inputs
    # Deleter
    def del_data(self):
        self._data = ""
    # Adder
    def add_data(self, inps):
        self._data += inps
    # Result getter
    def get_result(self):
        return self._result
    # Result setter
    def set_result(self, inb):
        self._result = inb
# Instance
dS = DataStorage()
# Calculator Logic

def key_pressed_check(ex):
    if ex == '1':
        press('1')
    elif ex == '2':
        press('2')
    elif ex == '3':
        press('3')
    elif ex == '4':
        press('4')
    elif ex == '5':
        press('5')
    elif ex == '6':	
        press('6')
    elif ex == '7':
        press('7')
    elif ex == '8':
        press('8')
    elif ex == '9':
        press('9')
    elif ex == '0':
        press('0')
    elif ex == '/':
        press('/')
    elif ex == '*':
        press('*')
    elif ex == '-':
        press('-')
    elif ex == '+':
        press('+')
    elif ex == '.':
        press('.')
    elif ex == 'π':
        press('π')
    elif ex == '=':
        equals()
        
# Operation Logic
def press(button_clicked):
    if dS.get_data() == '0' and button_clicked == '0':
        dS.set_data('0')
    elif dS.get_data() == '0':
        dS.set_data(button_clicked)
    else:
        dS.add_data(button_clicked)
    print(dS.get_data()) # For output check
def cls():
    dS.del_data()
    dS.set_data('0')
    dS.set_result('0')
    print(dS.get_data()) # For output check

def dels():
    x = dS.get_data()
    x = x[:-1]
    dS.set_data(x)
    # print(dS.get_data()) # For output check

def equals():
    PI = str(pi)
    result = str(eval(dS.get_data().replace('π', PI)))
    print(result) # For output check
    dS.set_result(result)

# Key press event
def key_press(event):
    pressed = event.char
    key_pressed_check(pressed)
    # print(pressed, ' is pressed.')

def copy2Clip():
    coppy = str(dS.get_result())
    print(coppy)
    subprocess.run(['clip.exe'], input= coppy.strip().encode('utf-16'), check=TRUE)
