# Author: Jien Huang
# Date: 2022-04-01
# Description: Test Automation Management UI

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def show_msg(title='warning', msg='Not implemented yet'):
    messagebox.showinfo(title, msg)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # root window
        self.title("Test Automation Management UI")
        self.geometry("1024x768")
        self.style = ttk.Style(self)
        self.style.theme_use("alt") # winnative clam alt default classic vista xpnative

        # tabs
        tab_control = ttk.Notebook(self)
        tabSettings = ttk.Frame(tab_control)
        tabInstances = ttk.Frame(tab_control)
        tabScripts = ttk.Frame(tab_control)
        tabLogs = ttk.Frame(tab_control)
        tab_control.add(tabSettings, text='Settings')
        tab_control.add(tabInstances, text='Instances')
        tab_control.add(tabScripts, text='Scripts')
        tab_control.add(tabLogs, text='Logs')

        # tabSettings - command buttons line, settings table
        settingsRefreshButton = ttk.Button(tabSettings, text='Refresh', command=show_msg)
        settingsRefreshButton.grid(column=0, row=0)
        settingsSaveButton = ttk.Button(tabSettings, text='Save', command=show_msg)
        settingsSaveButton.grid(column=1, row=0)
        set = ttk.Treeview(tabSettings, height=10, columns=('Setting', 'Value'))
        set.grid(row=1, sticky='nsew')
        data = [('Setting 1', 'Value 1'), ('Setting 2', 'Value 2'), ('Setting 3', 'Value 3')]

        for record in data:
            set.insert('', 'end', values=record)



        # tabInstances - command buttons line, instances table
        instancesRefreshButton = ttk.Button(tabInstances, text='Refresh', command=show_msg)
        instancesRefreshButton.grid(column=0, row=0)
        # instancesSaveButton = ttk.Button(tabInstances, text='Save', command=show_msg)
        # instancesSaveButton.grid(column=1, row=0)

        # tabScripts - command buttons line, scripts tree
        scripsRefreshButton = ttk.Button(tabScripts, text='Refresh', command=show_msg)  
        scripsRefreshButton.grid(column=0, row=0)
        scriptsRunButton = ttk.Button(tabScripts, text='Run', command=show_msg)
        scriptsRunButton.grid(column=1, row=0)


        # tabLogs - command buttons line, logs table
        logsRefreshButton = ttk.Button(tabLogs, text='Refresh', command=show_msg)
        logsRefreshButton.grid(column=0, row=0)
        logsDeleteButton = ttk.Button(tabLogs, text='Delete', command=show_msg)
        logsDeleteButton.grid(column=1, row=0)

        tab_control.pack(expand=1, fill='both')


    



if __name__ == '__main__':
    app = App()
    app.mainloop()