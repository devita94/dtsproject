import tkinter as tk
from tkinter import *
import tkinter
from mypackage import dictionary

window = tk.Tk()
window.title("KBBI Apps")

#untuk window
frame = tk.Frame(master=window, bg="#317FE2")
frame.pack(fill=tk.BOTH, expand=TRUE)
title_frame = tk.Label(master = frame, text="Selamat Datang di KBBI Apps", bg="#317FE2")
title_frame.pack()
input_label = tk.Label(
    text="Silakan cari kata dengan mengetikkan pada kolom dibawah ini"
)
input_label.pack(expand=TRUE)
frm_entry = tk.Entry()
frm_entry.pack(fill=tk.BOTH, expand=TRUE)
btn_submit = tk.Button(
    text="Cari",
    width=50,
    height=20,
    bg="blue",
    fg="white",
)
btn_submit.pack()

def check_input():
    user_input = frm_entry.get()
    #if user_input in find_word():
    return user_input

window.mainloop()
