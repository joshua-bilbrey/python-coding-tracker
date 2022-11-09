import datetime
from math import floor
from tkinter import *
from tkinter import messagebox
from pixela import update_pixel, delete_pixel, post_pixel

FONT = ("Courier", 28, "bold")
GREY = "#2f2f2f"

timer_on = False
timer = 0
clock = None
date = datetime.datetime.now().strftime("%Y%m%d")
print(date)


# functions
def add_second():
    global timer, clock
    timer += 1
    minutes = floor(timer / 60)
    if minutes < 60:
        if minutes != 0:
            seconds = timer % 60
        else:
            seconds = timer
        if minutes < 10:
            minutes = f"0{minutes}"
        if seconds < 10:
            seconds = f"0{seconds}"
        timer_label.config(text=f"{minutes}:{seconds}")
    else:
        hours = floor(timer / 3600)
        minutes = floor((timer % 3600) / 60)
        if hours < 10:
            hours = f"0{hours}"
        if minutes < 10:
            minutes = f"0{minutes}"
        timer_label.config(text=f"{hours}:{minutes}")
    clock = window.after(1000, func=add_second)


def start_pause():
    global timer_on
    if not timer_on:
        timer_on = True
        pause_btn.config(text="Pause")
        add_second()
    else:
        timer_on = False
        pause_btn.config(text="Start")
        window.after_cancel(clock)


def add():
    if messagebox.askokcancel(title="Add Time", message=f"You are adding {round(timer /60)} minutes of python coding "
                                                        f"as your total coding time for today."):
        post_pixel(date, timer / 60)


# opens new window to update or delete Pixela data
def update():
    def error_message():
        messagebox.showerror("Format Error", message="Please enter date as 'YYYYmmdd' and time spent in minutes.")

    def confirm_message(update_date: datetime.date, quantity=None):
        if quantity:
            return messagebox.askokcancel(title="Update Date",
                                          message=f"You are updating {update_date.strftime('%B')} {update_date.day}, "
                                                  f"{update_date.year} with {quantity} minutes of python coding.")
        else:
            return messagebox.askokcancel(title="Delete Date",
                                          message=f"You are deleting all saved date for {update_date.strftime('%B')} "
                                                  f"{update_date.day}, {update_date.year}.")

    def call_update():
        date_string = date_entry.get()
        if len(date_string) == 8:
            try:
                new_date = datetime.datetime.strptime(date_string, "%Y%m%d")
                new_time = float(quantity_entry.get())
            except ValueError:
                error_message()
            else:
                if confirm_message(update_date=new_date, quantity=new_time):
                    update_pixel(date_string, new_time)
                    new_window.destroy()

    def call_delete():
        date_string = date_entry.get()
        if len(date_string) == 8:
            try:
                new_date = datetime.datetime.strptime(date_string, "%Y%m%d")
            except ValueError:
                error_message()
            else:
                if confirm_message(new_date):
                    delete_pixel(date_string)
                    new_window.destroy()

    new_window = Tk()
    new_window.title("Update Pixela")
    new_window.config(padx=30, pady=30, bg="black")

    date_label = Label(new_window, text="Select date to update: ", bg="black", fg="white")
    date_label.pack()
    date_entry = Entry(new_window)
    date_entry.insert(END, "YYYYmmdd")
    date_entry.pack(pady=10)

    quantity_label = Label(new_window, text="Enter time spent on Python: ", bg="black", fg="white")
    quantity_label.pack()
    quantity_entry = Entry(new_window)
    quantity_entry.insert(END, "Time in minutes...")
    quantity_entry.pack(pady=10)

    update_pixel_btn = Button(new_window, text="Update",
                              bg=GREY, fg="white", activebackground=GREY, activeforeground="white",
                              command=call_update)
    update_pixel_btn.pack(pady=10)
    delete_pixel_btn = Button(new_window, text="Delete",
                              bg=GREY, fg="white", activebackground=GREY, activeforeground="white",
                              command=call_delete)
    delete_pixel_btn.pack()


# create UI
window = Tk()
window.title("Python Tracking")
window.config(padx=30, pady=30, bg="white", width=457, height=704)

canvas = Canvas(width=397, height=534, highlightthickness=0)
hourglass = PhotoImage(file="images/hourglass.gif")
canvas.create_image(0, 0, image=hourglass, anchor="nw")
canvas.place(x=0, y=90)

title_canvas = Canvas(width=397, height=90, highlightthickness=0)
title_image = PhotoImage(file="images/title.gif")
title_canvas.create_image(0, 0, image=title_image, anchor="nw")
title_canvas.place(x=0, y=0)

timer_label = Label(text="00:00", bg="black", fg="white", font=FONT)
timer_label.place(x=140, y=200)

pause_btn = Button(text="Start", bg=GREY, fg="white", activebackground=GREY, activeforeground="white",
                   command=start_pause)
pause_btn.place(x=150, y=480)

add_btn = Button(text="Done", bg=GREY, fg="white", activebackground=GREY, activeforeground="white", command=add)
add_btn.place(x=210, y=480)

update_btn = Button(text="Update Other Time", bg=GREY, fg="white", activebackground=GREY, activeforeground="white",
                    command=update)
update_btn.place(x=145, y=560)

window.mainloop()
