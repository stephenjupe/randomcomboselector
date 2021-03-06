#########################################################################
#                                                                       #
# RandomComboSelector.py                                                #
#                                                                       #
# This file is the main executable for the Random Combination Selector. #
#                                                                       #
#########################################################################

import sys
import random
import tkinter #we can also do aliasing here, such as "import tkinter as tk" or more dangerously "from tkinter import *"

class RandomComboSelector(tkinter.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.hi_there = tkinter.Button(self)
		self.hi_there["text"] = "Print Message"
		self.hi_there["command"] = self.say_hi
		self.hi_there.pack(side="top")
		self.quit = tkinter.Button(self, text="Quit", command=self.master.destroy)
		self.quit.pack(side="bottom")

	def say_hi(self):
		print("Hi there, everyone!")
		print("It's a great day today!")

root = tkinter.Tk()
root.geometry("500x200") #default window size increase so it doesn't start tiny

app = RandomComboSelector(master=root)
# app.master.maxsize(1000,400) #Can make a max size for the window as well
app.master.title("Random Combination Selector")
app.mainloop()

#function that creates random length of chars from 1-10
def random_selector_func ():
    #create random length
    rand_str_len = random.randrange(1,11)
    
    #add random characters until you reach rand_str_len
    output_str = ''
    while rand_str_len != 0:
        output_str += random.choice("abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*")
        rand_str_len -= 1
        
    return output_str
