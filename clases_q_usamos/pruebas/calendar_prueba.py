# Import Required Library
import datetime
from tkinter import *
from tkcalendar import Calendar

# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")

# Add Calendar
calendarioDesde = Calendar(root, selectmode='day',
                           year=datetime.datetime.now().year, month=datetime.datetime.now().month,
                           day=datetime.datetime.now().day)

calendarioHasta = Calendar(root, selectmode='day',
               year=2020, month=5,
               day=22)

calendarioDesde.pack(pady=20)


def grad_date():
    date.config(text="Selected Date is: " + calendarioHasta.get_date())


# Add Button and Label
Button(root, text="Get Date",
       command=grad_date).pack(pady=20)

date = Label(root, text="")
date.pack(pady=20)

# Execute Tkinter
root.mainloop()