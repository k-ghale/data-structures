
#Create the GUI Elements
import tkinter
from tkinter import messagebox
import random

#Create root window
root = tkinter.Tk()

#Change root window background color
root.configure(bg="white")

#Change the Title
root.title("My To-Do-List ")

#Change window size
root.geometry("325x275")

#Create an empty List
tasks = []

#For testing purpose
#tasks = ["Call","Go","Do"]

#Create Functions

def update_listbox():
    clear_listbox()
    #populate the listbox
    for task in tasks:
        lb_tasks.insert("end", task)

def clear_listbox():
    lb_tasks.delete(0, "end")

def add_task():
    task = txt_input.get()
    if task!='':
        tasks.append(task)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "You need to enter a task.")
    txt_input.delete(0, "end")

def del_all():
    confirmed = messagebox.askyesno("Please Confirm", "Do you really want to delete all?")
    if confirmed:
    #Since we are changing the list, it needs to be global
        global tasks
    #clear the tasklist
        tasks = []
        update_listbox();

def del_one():
    task = lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
    update_listbox()


def sort_asc():
    #Sort the list
    tasks.sort()
    update_listbox()


def sort_desc():
    #Sort the list
    tasks.sort()
    #Reverse the list
    tasks.reverse()
    #update
    update_listbox()

def choose_random():
    #Choose a random task
    task = random.choice(tasks)
    #update
    lbl_display["text"] = task


def number_of_task():
    number_of_task = len(tasks)
    #Create and format the message
    msg = "Number of tasks : %s" %number_of_task
    lbl_display["text"] = msg


def exit():
    confirmed = messagebox.askyesno("Please Confirm", "Do you really want to exit?")
    if confirmed:
        root.destroy()

lbl_title = tkinter.Label(root, text="To-Do-List", bg = "white")
lbl_title.grid(row=0,column=0)

lbl_display = tkinter.Label(root, text="", bg = "white")
lbl_display.grid(row=0,column=1)

txt_input = tkinter.Entry(root, width=15)
txt_input.grid(row=1,column=1)


btn_add_task = tkinter.Button(root, text="Add task", fg="green", bg="white", command=add_task)
btn_add_task.grid(row=1,column=0)



btn_delete_all= tkinter.Button(root, text="Delete All", fg="green", bg="white", command=del_all)
btn_delete_all.grid(row=2,column=0)



btn_del_one= tkinter.Button(root, text="Delete", fg="green", bg="white", command=del_one)
btn_del_one.grid(row=3,column=0)



btn_sort_asc= tkinter.Button(root, text="Sort Ascending", fg="green", bg="white", command=sort_asc)
btn_sort_asc.grid(row=4,column=0)



btn_sort_desc= tkinter.Button(root, text="Sort Desending", fg="green", bg="white", command=sort_desc)
btn_sort_desc.grid(row=5,column=0)



btn_choose_random= tkinter.Button(root, text="Choose Random", fg="green", bg="white", command=choose_random)
btn_choose_random.grid(row=6,column=0)



btn_number_of_task= tkinter.Button(root, text="Number of Tasks", fg="green", bg="white", command=number_of_task)
btn_number_of_task.grid(row=7,column=0)



btn_exit= tkinter.Button(root, text="Exit", fg="green", bg="white", command=exit)
btn_exit.grid(row=8,column=0)


lb_tasks = tkinter.Listbox(root)
lb_tasks.grid(row=2,column=1, rowspan=7)


#Start the main events loop
root.mainloop()
