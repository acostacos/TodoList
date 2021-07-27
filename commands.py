from tkinter import *
from datetime import date

# Global Varibales
TODO_ITEMS = []


def get_current_date():
    today = date.today()
    return today.strftime('%B %d, %Y')


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def complete_task_action(body, selection):
    if len(selection) > 0:
        index = selection[0]
        TODO_ITEMS.pop(index)
        set_body(body, 'home')


def add_task_action(body, task):
    if task != "":
        TODO_ITEMS.append(task)
        set_body(body, 'home')


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

        for item in TODO_ITEMS:
            tasks_listbox.insert(END, item)

        comp_navbtn = Button(body, text="Complete", width=26,
                             command=lambda: complete_task_action(body, tasks_listbox.curselection()))
        comp_navbtn.pack(side=BOTTOM)
    if page == 'add':
        name_label = Label(body, text='Task Name')
        name_label.pack(anchor="w")

        name_entry = Entry(body, width=30)
        name_entry.pack(padx=5, anchor="w")

        add_button = Button(body, text="Add Task",
                            command=lambda: add_task_action(body, name_entry.get()))
        add_button.pack()
