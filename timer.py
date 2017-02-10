#!/usr/local/bin/python3

'''
python timer demo
'''

#encodin: UTF-8

import threading
import tkinter
from time import ctime


def popwin():
	root = tkinter.Tk()
	root.title("Test Automation")
	root.minsize(800, 400)
	app = tkinter.Frame(root)
	app.pack()
	button = tkinter.Button(app)
	button["text"] = "Hello World\n(click me)"
	button["command"] = sayHi
	button.pack(side="top")
	app.mainloop()

def func():
	print('hello time is: %s' % ctime())


def sayHi():
	print('hi button clicked!')

timer = threading.Timer(5,func)
timer.start()

popwin()
