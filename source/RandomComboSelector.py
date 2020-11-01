#########################################################################
#                                                                       #
# RandomComboSelector.py                                                #
#                                                                       #
# This file is the main executable for the Random Combination Selector. #
#                                                                       #
#########################################################################

import sys
import random
import tkinter

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

root = tkinter.Tk()
app = RandomComboSelector(master=root)
app.mainloop()
