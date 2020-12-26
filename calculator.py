#import tkinter
from tkinter import *



if __name__ == "__main__":
    #create window
    window = Tk()
    window.title('Calculator!')
    window.geometry('400x200x400x200')

    user_input = StringVar()
    input_entry = Entry(window, font=('arial', 20, 'bold'), bd=30, bg='gray', width=20, textvariable = user_input)
    input_entry.grid(row=0, columnspan=4, sticky=(W, E))

    # create button for 1-9 and '+', '-', '*', '/', '=', '.', 'clear'
    btn1 = Button(window, text = ' 1 ', font=('arial', 20, 'bold'), bd=5, width=6, height=1, command=lambda : press(1))
    btn1.grid(row=2, column=0)

    window.mainloop()

