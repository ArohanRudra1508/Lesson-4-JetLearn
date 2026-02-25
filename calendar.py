from tkinter import *
from tkinter.ttk import *
import calendar

def showCalendar():

    root = Toplevel()
    root.config(background = "white")
    root.geometry("550x600")
    root.title("CALENDAR")

    try:
        year = int(ent.get())
        cal = calendar.calendar(year)
        text_area = Text(root, font = ("Consolas", 14))

        text_area.insert(END, cal)
        text_area.config(state = DISABLED)
        text_area.pack(expand = True, fill = BOTH)

        sb = Scrollbar(root, command = text_area.yview)
        sb.pack(side = RIGHT, fill = Y)
        sb.config(yscrollcommand = sb.set)

    except ValueError:
        LAB = Label(root, text = "Please enter a valid year!", fg = "pink", bg = "red")


if __name__ == "__main__":
    win = Tk()

    win.columnconfigure(0, weight = 1)
    win.columnconfigure(1, weight = 1)
    win.columnconfigure(2, weight = 1)

    win.geometry("300x300")
    win.title("Calendar")
    lab = Label(win, text = "Calendar", font = ("Poppins", 20))
    lab.grid(row = 0, column = 1, pady = 10)

    lab2 = Label(win, text = "Enter the year:")
    ent = Entry(win, text = "Year no.")
    lab2.grid(row = 1, column = 1, pady = 10)
    ent.grid(row = 2, column = 1, pady = 10)

    but = Button(win, text = "Show Calendar", command = showCalendar)
    but.grid(row = 3, column = 1)
    but2 = Button(win, text = "Exit")
    but2.grid(row = 4, column = 1)

    win.mainloop()
