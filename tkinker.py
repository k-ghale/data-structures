
import tkinter as tk

root = tk.Tk()

root.title("Count All")

button = tk.Button(root, text = "Stop", width = 25, command = root.destroy)
button.pack()

label = tk.Label(root, text = "Top")
label2 = tk.Label(root , text = "Bottom")

#pack with parameters
label.pack(side = tk.TOP, fill = tk.X , padx = 10, pady = 10)
label2.pack(side = tk.BOTTOM, fill = tk.X , padx = 10, pady = 10)

root.mainloop()
