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
root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_X}+{WINDOW_Y}')

# Main Parts
header = Frame(root, height=100, width=WINDOW_WIDTH)
body = Frame(root, bg="yellow", height=100, width=WINDOW_WIDTH)
navbar = Frame(root, height=100, width=WINDOW_WIDTH)

# Header
date_text = StringVar()
app_label = Label(header, text="TodoList", font=(APP_FONT, '24', 'bold'))
date_label = Label(header, textvariable=date_text, font=(APP_FONT, '16'))
date_text.set(get_current_date())

# Body
task = Frame(body)
checkbox = Checkbutton(task, text='Test Task')

# Navbar
add_navbtn = Button(navbar, text="Add", width=9)
cal_navbtn = Button(navbar, text="Calendar", width=9)
tags_navbtn = Button(navbar, text="Tags", width=9)
del_navbtn = Button(navbar, text="Deleted", width=9)


# Render
header.grid(row=0, column=0, columnspan=4, rowspan=2)
body.grid(row=2, column=0, columnspan=4, rowspan=4)
navbar.grid(row=6, column=0, columnspan=4, rowspan=2)

app_label.grid(row=0, column=0)
date_label.grid(row=1, column=0)

task.grid(row=0, column=0)
checkbox.grid(row=0, column=0)

add_navbtn.grid(row=0, column=0, columnspan=1)
cal_navbtn.grid(row=0, column=1, columnspan=1)
tags_navbtn.grid(row=0, column=2, columnspan=1)
del_navbtn.grid(row=0, column=3, columnspan=1)

root.mainloop()
