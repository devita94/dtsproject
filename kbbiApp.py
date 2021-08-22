import tkinter as tk
from tkinter.constants import TRUE, X
from typing import Text

window = tk.Tk()
window.title("KBBI Apps")

#untuk window
frame = tk.Frame(master=window, bg="white")
frame.pack(fill=tk.BOTH, expand=TRUE)
title_frame = tk.Label(master = frame, text="Selamat Datang di KBBI Apps", bg="#317FE2")
input_label = tk.Label(
    text="Cari Kata",
    foreground="black",  
    background="white",
    width=100,
    height=30
)
frm_entry = tk.Entry()
btn_submit = tk.Button(
    text="Cari",
    width=50,
    height=20,
    bg="blue",
    fg="white",
)


def find_word():
    worddict = {
        "ayah" : "orang tua kandung laki-laki; bapak",
        "ibu" : "wanita yang telah melahirkan seseorang",
        "anak" : " orang yang berasal dari atau dilahirkan di (suatu negeri, daerah, dan sebagainya)"
    }
    return worddict

def check_input():
    user_input = frm_entry.get()
    #if user_input in find_word():
    return user_input

window.mainloop()
