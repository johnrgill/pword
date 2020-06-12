# !/usr/bin/python3
import string
import random 
import tkinter
from tkinter import Button, Label, Entry
#password generator 

#gui stuff
top = tkinter.Tk()
top.title("Password Generator")
top.geometry("250x250")
#text field input
entry = Entry(top)
entry.place(x=75, y=38)

#label
label = Label(top, text="How many chars?")
label.place(x=75, y=20)

#text field output
entry_output = Entry(top)
entry_output.place(x=75, y=105)

#function to generate password
def password():
	#delete previous password for multiple uses
	entry_output.delete(0, 'end')
	try:
		length = int(entry.get())
		chars = string.punctuation + string.digits + string.ascii_letters
		pword = "".join(random.sample(chars,length))
		entry_output.insert(0, pword)
	except:
		entry_output.insert(0, 'please enter an integer')

#button
B = Button(top, text="generate", command=password)
B.place(x=75, y=75)
top.mainloop()

	
	
