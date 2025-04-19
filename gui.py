from tkinter import *
root = Tk()
root.title("simply calculator")

e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
# e.insert(0,"username: ")

def myClick(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    firstnum = e.get()
    global fnum
    global math
    math ="addition"
    fnum= int(firstnum)
    e.delete(0,END)

def button_equal():
    second_number=e.get()
    e.delete(0,END)

    if math=="addition":
        e.insert(0,fnum + int(second_number))
    if math=="subtraction":
        e.insert(0,fnum - int(second_number))
    if math=="multiplication":
        e.insert(0,fnum * int(second_number))
    if math=="division":
        e.insert(0,fnum / int(second_number))

def sub():
    firstnum = e.get()
    global fnum
    global math
    math ="subtraction"
    fnum= int(firstnum)
    e.delete(0,END)

def multiply():
    firstnum = e.get()
    global fnum
    global math
    math ="multiplication"
    fnum= int(firstnum)
    e.delete(0,END)

def division():
    firstnum = e.get()
    global fnum
    global math
    math ="division"
    fnum= int(firstnum)
    e.delete(0,END)

button1 = Button(root,text = "1" , command=lambda: myClick(1),padx=40,pady=20)
button2 = Button(root,text = "2" , command=lambda: myClick(2),padx=40,pady=20)
button3 = Button(root,text = "3" , command=lambda: myClick(3),padx=40,pady=20)
button4 = Button(root,text = "4" , command=lambda: myClick(4),padx=40,pady=20)
button5 = Button(root,text = "5" , command=lambda: myClick(5),padx=40,pady=20)
button6 = Button(root,text = "6" , command=lambda: myClick(6),padx=40,pady=20)
button7 = Button(root,text = "7" , command=lambda: myClick(7),padx=40,pady=20)
button8 = Button(root,text = "8" , command=lambda: myClick(8),padx=40,pady=20)
button9 = Button(root,text = "9" , command=lambda: myClick(9),padx=40,pady=20)
button0 = Button(root,text = "0" , command=lambda: myClick(0),padx=40,pady=20)
buttonadd = Button(root,text = "+" , command=button_add,padx=40,pady=20)
buttonclear = Button(root,text = "C" , command=button_clear,padx=40,pady=20)
buttonmultiply = Button(root,text = "*" , command=multiply,padx=40,pady=20)
buttonsub = Button(root,text = "-" , command=sub,padx=40,pady=20)
buttondivide = Button(root,text = "/" , command=division,padx=40,pady=20)
buttoneq = Button(root,text = "=" , command=button_equal,padx=40,pady=20)

button1.grid(row=3,column=1)
button2.grid(row=3,column=2)
button3.grid(row=3,column=3)
button4.grid(row=2,column=1)
button5.grid(row=2,column=2)
button6.grid(row=2,column=3)
button7.grid(row=1,column=1)
button8.grid(row=1,column=2)
button9.grid(row=1,column=3)
button0.grid(row=1,column=1)
buttonadd.grid(row=4,column=1)
buttonclear.grid(row=4,column=2)
buttonmultiply.grid(row=4,column=3)
buttonsub.grid(row=5,column=1)
buttondivide.grid(row=5,column=2)
buttoneq.grid(row=5,column=3)

root.mainloop()
