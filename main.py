from tkinter import *
from tkinter import messagebox
timer = None


window = Tk()
window.title("Disappearing Text")
window.config(pady=20, padx=20)


warning_label = None
time_label = None


text = Text(font=("Courier", 20, "normal"))
text.grid(row=1, columnspan=2, column=0)

def any_key(key):
    global timer
    if timer is not None:
        window.after_cancel(timer)

    timer = window.after(1000, countdown, 5)

def countdown(count):
    global warning_label, time_label
    if count == 5:
        warning_label = Label(text="Text is going to dissappear after...  ")
        time_label = Label(text=f"{count}", foreground="red")
        warning_label.grid(row=0, column=0, sticky="e", pady=10)
        time_label.grid(row=0, column=1, sticky="w")
        window.after(1000, countdown, count-1)
    elif 0 < count < 5:
        time_label.config(text=f"{count}")
        window.after(1000, countdown, count-1)
    else:
        delete_text()


def delete_text():
    global warning_label, time_label
    warning_label.destroy()
    time_label.destroy()
    text.delete('1.0', END)


window.bind("<Key>", any_key)

messagebox.showwarning(title="Warning", message="The Most Dangerous Writing app..\n Don't stop wrinting or all progress will be lost!")


window.mainloop()