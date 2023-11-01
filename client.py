import tkinter as tk
from socket import *

win = tk.Tk()

def click():
    client.send(bytes("\00", 'ascii'))

def create_widget():
    win.title('POPcat')
    win.geometry("500x300+400+300")
    win.config(bg='#C45B90')
    win.resizable(width=False, height=False)
    btn = tk.Button(win, text='POP and see what comes next', width=100, height=100, command=click)
    btn.place(relx=0.5, rely=0.5, anchor='center')
    win.mainloop()

client = socket(AF_INET, SOCK_STREAM)
client.connect(('172.20.10.4', 6543))
create_widget()
client.close()
close()