from tkinter import *
from tkinter.ttk import *
import calendar

if __name__ == "__main__":
    win = Tk()
    win.geometry("300x300")
    win.title("Calendar")
    lab = Label(win, text = "Calendar", font = ("Poppins", 20))
    lab.grid(row = 0, column = 1, pady = 10, columnspan = 5)

    lab2 = Label(win, text = "Enter the year:")
    ent = Entry(win, text = "Year no.")
    lab2.grid(row = 1, column = 1, pady = 10)
    ent.grid(row = 2, column = 1, pady = 10)

    but = Button(win, text = "Show Calendar", bg = "blue", fg = "orange")
    but.grid(row = 3, column = 1)
    but2 = Button(win, text = "Exit", bg = "blue", fg = "orange")
    but2.grid(row = 4, column = 1)



    win.mainloop()