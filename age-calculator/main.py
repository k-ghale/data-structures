import tkinter as tk
from tkinter import messagebox;

root = tk.Tk()

root.title("Age Calculator")

root.geometry("300x300")

#Calculate Age
def calculate_age():
    current_year = 2024
    given_year = lbl_input.get()
    if given_year == '':
        messagebox.showwarning("Warning", "Please give your birth-year.") 
    else:
        given_year = int(given_year)
        if given_year<2000:
            messagebox.showwarning("Warning","Please enter a valid birth-year.")
            lbl_input.delete(0,"end")
        else:
            current_age = current_year - given_year
            lbl_display["text"] = current_age
    lbl_input.delete(0,"end")

#Exit Program
def exit_now():
    msg = messagebox.askyesno("Warning", "Do you really want to exit?")
    if msg:
        root.destroy()

#Age Label
lbl_label1 = tk.Label(root, text="Enter your birth year :")
lbl_label1.pack()

#Age Input
lbl_input = tk.Entry(root)
lbl_input.pack()

#Button to Calculate the age
lbl_button = tk.Button(root, text="Calculate", width=25, command=calculate_age)
lbl_button.pack()

#Display
lbl_display = tk.Label(root, text="" , bg="white")
lbl_display.pack()

#Exit button
lbl_exit = tk.Button(root, text="Exit", width=10, command=exit_now)
lbl_exit.pack()

#Mainloop
root.mainloop()