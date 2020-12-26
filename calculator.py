#import tkinter
from tkinter import *

#create window
window = Tk()

# create button for 1-9 and '+', '-', '*', '/', '=', '.', 'clear'
btn1 = Button(window, text = ' 1 ', font=('arial', 20, 'bold'), bd=5, width=6, height=1, command=lambda : press(1))
btn1.grid(row=2, column=0)

window.mainloop()