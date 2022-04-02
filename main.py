# Author: Jien Huang
# Date: 2022-04-01
# Description: Test Automation Management UI

from tkinter import *

from tkinter import ttk

window = Tk()

window.title("Test Automation Manager")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)

tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Settings')

tab_control.add(tab2, text='Instances')

lbl1 = Label(tab1, text= 'label1')

lbl1.grid(column=0, row=0)

lbl2 = Label(tab2, text= 'label2')

lbl2.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')

window.geometry('800x600')
window.mainloop()