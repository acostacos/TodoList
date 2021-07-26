from tkinter import *
from datetime import date


def get_current_date():
    today = date.today()
    return today.strftime('%B %d, %Y')


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def add_task_actions():
    pass


def set_body(body, page):
    clear_frame(body)
    if page == 'home':
        tasks_frame = Frame(body)
        tasks_frame.pack()

        tasks_listbox = Listbox(tasks_frame, height=23, width=29)
        tasks_listbox.pack(side=LEFT)

        tasks_scrollbar = Scrollbar(tasks_frame)
        tasks_scrollbar.pack(side=RIGHT, fill=Y)
        tasks_listbox.config(yscrollcommand=tasks_scrollbar.set)
        tasks_scrollbar.config(command=tasks_listbox.yview)

        comp_navbtn = Button(body, text="Complete", width=26)
        comp_navbtn.pack(side=BOTTOM)
    if page == 'add':
        name_label = Label(body, text='Task Name')
        name_label.pack(anchor="w")

        name_entry = Entry(body, width=30)
        name_entry.pack(padx=5, anchor="w")

        add_button = Button(body, text="Add Task")
        add_button.pack()
