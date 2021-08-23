import tkinter as tk
from tkinter import *
import tkinter
from typing import Any
from mypackage import dictionary

window = tk.Tk()
window.title("KBBI Apps")

#untuk window
frame = tk.Frame(master=window, bg="blue", width=300, height=300)
frame.pack(fill=tk.BOTH, expand=TRUE)
title_frame = tk.Label(master = frame, text="Selamat Datang di KBBI Apps", bg="#317FE2")
title_frame.pack()
input_label = tk.Label(
    text="Silakan cari kata dengan mengetikkan pada kolom dibawah ini"
)
input_label.pack(expand=TRUE)
frm_entry = tk.Entry()
frm_entry.pack(fill=tk.BOTH, expand=TRUE)
btn_submit = tk.Button(text="Cari", background="#317FE2", width=30, height=10)
btn_submit.pack()

def check_input():
    user_input = frm_entry.get()
    if user_input in dictionary.myDictionary(myWord=Any):
        try:
            print(dictionary.myDictionary(myWord=Any))
            print(dictionary.myDictionary(mySynonym=Any))
        except:
            print("Kata Tidak ditemukan")
    return user_input

window.mainloop()
