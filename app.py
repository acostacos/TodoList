from tkinter import *
from commands import get_current_date

# Constants
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 300
WINDOW_X = 100
WINDOW_Y = 100
APP_FONT = 'Helvetica'

# Main Loop
root = Tk()
root.title('TodoList')
root.resizable(False, False)
root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_X}+{WINDOW_Y}')

# Main Parts
header = Frame(root, height=WINDOW_HEIGHT, width=WINDOW_WIDTH//2)
header.grid(row=0, column=0, columnspan=2)
body = Frame(root, height=WINDOW_HEIGHT, width=WINDOW_WIDTH//2)
body.grid(row=0, column=2, columnspan=2)

# Header
app_label = Label(header, text='TodoList', font=(APP_FONT, '12'), width=10)
app_label.pack()

date_text = StringVar()
date_label = Label(header, textvariable=date_text,
                   font=(APP_FONT, '12'), width=10)
date_text.set(get_current_date())
date_label.pack()

add_navbtn = Button(header, text="Add", width=13)
add_navbtn.pack()

cal_navbtn = Button(header, text="Calendar", width=13)
cal_navbtn.pack()

tags_navbtn = Button(header, text="Tags", width=13)
tags_navbtn.pack()

del_navbtn = Button(header, text="Deleted", width=13)
del_navbtn.pack()

# Body
tasks_listbox = Listbox(body, height=24, width=29)
tasks_listbox.pack(side=LEFT)

tasks_scrollbar = Scrollbar(body)
tasks_scrollbar.pack(side=RIGHT, fill=Y)
tasks_listbox.config(yscrollcommand=tasks_scrollbar.set)
tasks_scrollbar.config(command=tasks_listbox.yview)

root.mainloop()
