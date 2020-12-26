#import tkinter
from tkinter import *

exp = ''

#create press function
def press(n):
    global exp
    exp = exp + str(n)
    user_input.set(exp)

#create equal function
# and try block to catch error
def equal():
    try:
        global exp
        total = str(eval(exp))
        user_input.set(total)
        exp = ''
    except:
        user_input.set('sorry, Invalid Input')
        exp= ''



if __name__ == "__main__":
    #create window
    window = Tk()
    window.title('Calculator!')
    window.geometry('500x400')

    user_input = StringVar()
    input_entry = Entry(window, font=('arial', 20, 'bold'), bd=30, bg='gray', width=20, textvariable = user_input)
    input_entry.grid(row=0, columnspan=4, sticky=(W, E))

    # create button for 1-9 and '+', '-', '*', '/', '=', '.', 'clear'
    btn1 = Button(window, text = ' 1 ', font=('arial', 20, 'bold'), bd=5, width=6, height=1, command=lambda : press(1))
    btn1.grid(row=2, column=0)
    btn2 = Button(window, text = ' 2 ', font=('arial', 20, 'bold'), bd=5, width=6, height=1, command=lambda : press(2))
    btn2.grid(row=2, column=1)
    btn3 = Button(window, text = ' 3 ', font=('arial', 20, 'bold'), bd=5, width=6, height=1, command=lambda : press(3))
    btn3.grid(row=2, column=2)
    btn_add = Button(window, text = ' + ', font=('arial', 20, 'bold'), bd=5, width=6, height=1, command=lambda : press(' + '))
    btn_add.grid(row=2, column=3)
    btn4 = Button(window, text = ' 4 ', font=('arial', 20, 'bold'), bd=5, width=6, height=1, command=lambda : press(4))
    btn4.grid(row=3, column=0)
    btn5 = Button(window, text = ' 5 ', font=('arial', 20, 'bold'), bd=5, width=6, height=1, command=lambda : press(5))
    btn5.grid(row=3, column=1)
    btn6 = Button(window, text = ' 6 ', font=('arial', 20, 'bold'), bd=5, width=6, height=1, command=lambda : press( 6 ))
    btn6.grid(row=3, column=2)
    btn_sub = Button(window, text = ' - ', font=('arial', 20, 'bold'), bd=5, width=6, height=1, command=lambda : press(' - '))
    btn_sub.grid(row=3, column=3)
    btn7 = Button(window, text = ' 7 ', font=('arial', 20, 'bold'), bd=5, width=6, height=1, command=lambda : press(7))
    btn7.grid(row=4, column=0)
    btn8 = Button(window, text = ' 8 ', font=('arial', 20, 'bold'), bd=5, width=6, height=1, command=lambda : press(8))
    btn8.grid(row=4, column=1)
    btn9 = Button(window, text = ' 9 ', font=('arial', 20, 'bold'), bd=5, width=6, height=1, command=lambda : press(9))
    btn9.grid(row=4, column=2)
    btn_multi = Button(window, text = ' * ', font=('arial', 20, 'bold'), bd=5, width=6, height=1, command=lambda : press(' * '))
    btn_multi.grid(row=4, column=3)
    btn0 = Button(window, text = ' 0 ', font=('arial', 20, 'bold'), bd=5, width=6, height=1, command=lambda : press(0))
    btn0.grid(row=5, column=0)
    btn_dec = Button(window, text = ' . ', font=('arial', 20, 'bold'), bd=5, width=6, height=1, command=lambda : press(' . '))
    btn_dec.grid(row=5, column=1)
    btn_clr = Button(window, text = ' CLR ', font=('arial', 20, 'bold'), bd=5, width=6, height=1, command=lambda : press('CLR'))
    btn_clr.grid(row=5, column=2)
    btn_div = Button(window, text = ' / ', font=('arial', 20, 'bold'), bd=5, width=6, height=1, command=lambda : press('/'))
    btn_div.grid(row=5, column=3)
    btn_equal = Button(window, text = ' = ', font=('arial', 20, 'bold'), bd=5, width=6, height=1, command=equal)
    btn_equal.grid(row=6, column=3)
    
    


    window.mainloop()

