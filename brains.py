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
