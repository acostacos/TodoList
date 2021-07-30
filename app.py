from tkinter import *
from commands import load_todo_tasks, save_todo_tasks, get_current_date, set_body

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
root.protocol('WM_DELETE_WINDOW', lambda: save_todo_tasks(root))
load_todo_tasks()

# Main Parts
header = Frame(root, height=WINDOW_HEIGHT, width=WINDOW_WIDTH//3)
header.pack(side=LEFT)
header.pack_propagate(0)
body = Frame(root, height=WINDOW_HEIGHT, width=WINDOW_WIDTH*2//3)
body.pack(side=RIGHT)
body.pack_propagate(0)

# Header
app_label = Label(header, text='TodoList', font=(APP_FONT, '10'), width=10)
app_label.pack()

date_text = StringVar()
date_label = Label(header, textvariable=date_text,
                   font=(APP_FONT, '12', 'bold'), width=10)
date_text.set(get_current_date())
date_label.pack()

home_navbtn = Button(header, text="Home", width=13,
                     command=lambda: set_body(body, 'home'))
home_navbtn.pack()

add_navbtn = Button(header, text="Add", width=13,
                    command=lambda: set_body(body, 'add'))
add_navbtn.pack()

cal_navbtn = Button(header, text="Calendar", width=13)
cal_navbtn.pack()

# Future functionality

# tags_navbtn = Button(header, text="Tags", width=13)
# tags_navbtn.pack()

# del_navbtn = Button(header, text="Deleted", width=13)
# del_navbtn.pack()

# Body
set_body(body, 'home')

root.mainloop()
