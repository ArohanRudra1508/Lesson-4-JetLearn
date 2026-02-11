from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("250x250")

lab = Label(win, text = "I am a message box", font = ("Poppins", 60))
lab.pack()

messagebox.showinfo("Info", "Showing Information")

messagebox.showwarning("WARNING", "Showing WARNING")

messagebox.showerror("Error", "Showing Error")

win.mainloop()