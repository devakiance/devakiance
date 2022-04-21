from tkinter import *
import _tkinter
import tkinter as tk

master = Tk()
operator=""
master.title("Calculator")
text_input = StringVar()

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator=""


def createButtons():
    #===================================================================================================================
    tk.Button(master, text="7",command=lambda:btnClick(7),height= 4, width=11).grid(column=0, row=1,padx=5 , pady=5)
    tk.Button(master, text="8",command=lambda:btnClick(8),height= 4 ,width=11).grid(column=1, row=1,padx=5 , pady=5)
    tk.Button(master, text="9",command=lambda:btnClick(9),height= 4,width=11).grid(column=2, row=1,padx=5 , pady=5)
    tk.Button(master, text="+",command=lambda: btnClick("+"), height=4, width=11).grid(column=3, row=1, padx=5,pady=5)
    #===================================================================================================================
    tk.Button(master, text="4",command=lambda:btnClick(4),height= 4,width=11).grid(column=0, row=2,padx=5, pady=5)
    tk.Button(master, text="5",command=lambda:btnClick(5),height= 4,width=11).grid(column=1, row=2,padx=5, pady=5)
    tk.Button(master, text="6",command=lambda:btnClick(6),height= 4,width=11).grid(column=2, row=2,padx=5, pady=5)
    tk.Button(master, text="-", command=lambda: btnClick("-"), height=4, width=11).grid(column=3, row=2, padx=5,pady=5)
    #===================================================================================================================
    tk.Button(master, text="1",command=lambda:btnClick(1),height= 4,width=11).grid(column=0 ,row=3,padx=10 , pady=10)
    tk.Button(master, text="2",command=lambda:btnClick(2),height= 4,width=11).grid(column=1, row=3,padx=10 , pady=10)
    tk.Button(master, text="3",command=lambda:btnClick(3),height= 4,width=11).grid(column=2, row=3,padx=10 , pady=10)
    tk.Button(master, text="*",command=lambda: btnClick("*"), height=4, width=11).grid(column=3,row=3,padx=10,pady=10)
    #===================================================================================================================
    tk.Button(master, text="0",command=lambda:btnClick(0),height= 4,width=11).grid(column=0,row=4,padx=5,pady=5)
    tk.Button(master, text="C", command=lambda:btnClearDisplay(),height=4, width=11).grid(column=1,row=4, padx=5,pady=5)
    tk.Button(master, text="/",command=lambda:btnClick("/"),height= 4,width=11).grid(column=3,row=4,padx=5, pady=5)
    tk.Button(master, text="=",command=lambda:btnEquals(),height= 4 ,width=11).grid(column=2,row=4,padx=5, pady=5)
    #===================================================================================================================


textDisplay = Entry(master,font=('arial',20,'bold'), justify="right" , textvariable=text_input,bd=30, insertwidth=4,width=25).grid(row=0,column=0,columnspan=10)

createButtons()
